from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
import stripe
import json
import logging

from .forms import OrderForm
from .models import Order, OrderLineItem, PromoCode  
from events.models import Event
from profiles.models import UserProfile  
from bag.contexts import bag_contents

# Set up logging
logger = logging.getLogger(__name__)

@require_POST
def cache_checkout_data(request):
    try:
        client_secret = request.POST.get('client_secret')
        if not client_secret:
            raise ValueError("Client secret is required.")

        pid = client_secret.split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user.username if request.user.is_authenticated else None,
        })
        return HttpResponse(status=200)
    except Exception as e:
        logger.error(f"Error in cache_checkout_data: {e}")
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=str(e), status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        client_secret = request.POST.get('client_secret')

        if not client_secret:
            messages.error(request, 'Client secret is required for payment processing.')
            return redirect(reverse('view_bag'))

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)

            # Get or create user profile
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            order.user_profile = user_profile

            pid = client_secret.split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)

            # Initialize total and discount_amount
            total = 0
            discount_amount = 0

            # Calculate total from the bag
            for item_id, item_data in bag.items():
                try:
                    event = Event.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            event=event,
                            quantity=item_data,
                        )
                        order_line_item.save()
                        total += event.price * item_data
                except Event.DoesNotExist:
                    messages.error(request, (
                        "One of the Events in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Promo code logic
            promo_code_input = request.POST.get('promo_code', '').strip()

            if promo_code_input:
                try:
                    promo_code = PromoCode.objects.get(code=promo_code_input, active=True)
                    discount_amount = (promo_code.discount_percentage / 100) * total  # Calculate discount amount
                    messages.success(request, f"Promo code applied! You saved ${discount_amount:.2f}.")
                except PromoCode.DoesNotExist:
                    messages.error(request, "Invalid or expired promo code.")

            # Apply discount to total
            total -= discount_amount 
            total = max(0, total)  # Ensure total does not go negative
            order.order_total = total  
            order.grand_total = total  
            order.save()

            # Create a PaymentIntent
            stripe_total = round(total * 100)  # Stripe requires the amount in cents

            try:
                intent = stripe.PaymentIntent.create(
                    amount=stripe_total,
                    currency=settings.STRIPE_CURRENCY,
                )
                order.stripe_pid = intent.id
                order.save()
            except Exception as e:
                logger.error(f"Stripe PaymentIntent creation error: {e}")
                messages.error(request, 'There was an issue with the payment processing.')
                return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. Please double-check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)  # Total amount in cents
        stripe.api_key = stripe_secret_key

        try:
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            order_form = OrderForm()
        except Exception as e:
            logger.error(f"Stripe PaymentIntent creation error: {e}")
            messages.error(request, 'There was an issue with the payment processing.')
            return redirect(reverse('view_bag'))

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
