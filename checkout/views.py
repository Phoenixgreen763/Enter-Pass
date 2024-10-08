from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
import stripe
import json
import logging

from .forms import OrderForm
from .models import Order, OrderLineItem
from events.models import Event
from profiles.models import UserProfile  
from bag.contexts import bag_contents
from bag.views import calculate_grand_total

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

            # Get or create the user profile
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            order.user_profile = user_profile  # Associate the order with the user profile

            # Calculate grand total with discounts applied
            grand_total = calculate_grand_total(bag, request.session.get('discount_percentage', Decimal('0.00')))
            order.grand_total = grand_total  

            pid = client_secret.split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

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
                except Event.DoesNotExist:
                    messages.error(request, (
                        "One of the Events in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
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
        grand_total = current_bag['grand_total']  # Get grand total from the bag contents

        stripe_total = round(grand_total * 100)  
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
    View for order confirmation.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']
        
    bag = request.session.get('bag', {})
        
    discount_percentage = request.session.get('discount_percentage', Decimal('0.00'))
        
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'grand_total': order.grand_total, 
    }

    if 'discount_code' in request.session:
        del request.session['discount_code']
    if 'discount_percentage' in request.session:
        del request.session['discount_percentage']
            
    return render(request, template, context)