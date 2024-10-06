import stripe
from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from events.models import Event


stripe.api_key = settings.STRIPE_SECRET_KEY

def calculate_grand_total(bag):
    """Calculates the total price of items in the bag."""
    total = Decimal('0.00')
    for item_id, quantity in bag.items():
        try:
            event = Event.objects.get(pk=item_id)
            total += event.price * quantity
        except Event.DoesNotExist:
            continue  
    return total

def apply_coupon(request):
    """Apply coupon to the session-based bag"""
    if request.method == "POST":
        coupon_code = request.POST.get('coupon_code')

        try:
            coupon = stripe.Coupon.retrieve(coupon_code)
            discount = 0

            if coupon.percent_off:
                discount = Decimal(coupon.percent_off) / 100
            elif coupon.amount_off:
                discount = Decimal(coupon.amount_off) / 100 

            # Store the coupon and discount in the session
            request.session['coupon_code'] = coupon_code
            request.session['discount'] = discount
            messages.success(request, f'Coupon "{coupon_code}" applied successfully.')

        except stripe.error.InvalidRequestError:
            messages.error(request, 'Invalid coupon code.')

    return redirect('view_bag')

def view_bag(request):
    """A view that renders the bag contents page with coupon discount"""
    bag = request.session.get('bag', {})
    bag_items = []
    total = Decimal('0.00') 

    discount = request.session.get('discount', 0)

    for item_id, quantity in bag.items():
        try:
            event = Event.objects.get(pk=item_id)  
            subtotal = event.price * quantity  
            total += subtotal 
            bag_items.append({
                'event': event,
                'quantity': quantity,
                'subtotal': subtotal,
                'item_id': item_id
            })
        except Event.DoesNotExist:
            messages.error(request, f'Event with ID {item_id} does not exist.')

    # Calculate discount amount and apply to the grand total
    discount_amount = total * discount if discount else Decimal('0.00')
    grand_total = total - discount_amount

    context = {
        'bag_items': bag_items,
        'total': total,
        'discount_amount': discount_amount,
        'grand_total': grand_total,
        'coupon_code': request.session.get('coupon_code', None),
        'messages': messages.get_messages(request), 
    }

    return render(request, 'bag/bag.html', context)

def add_to_bag(request, item_id):
    """Add a quantity of the specified event to the shopping bag"""
    if request.method == "POST":
        event = get_object_or_404(Event, pk=item_id)

        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not specified
        redirect_url = request.POST.get('redirect_url', reverse('view_bag')) 

        # Initialize bag
        bag = request.session.get('bag', {})

        print(f'Adding item ID {item_id} to the bag. Quantity: {quantity}. Current bag: {bag}')

        # Check if the item already exists in the bag
        if str(item_id) in bag.keys():  
            bag[str(item_id)] += quantity
            messages.success(request, f'Updated {event.title} quantity to {bag[str(item_id)]}')
        else:
            bag[str(item_id)] = quantity
            messages.success(request, f'Added {event.title} to your bag')

        request.session['bag'] = bag
        print(f'Updated bag in session: {request.session.get("bag")}')
        return redirect(redirect_url)
    else:
        messages.error(request, 'Invalid request method.')
        return redirect(reverse('view_bag'))

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified event"""
    if request.method == "POST":
        event = get_object_or_404(Event, pk=item_id)
        quantity = int(request.POST.get('quantity', 0))  # Default to 0 if not specified
        bag = request.session.get('bag', {})

        print(f'Adjusting item ID {item_id}. New Quantity: {quantity}. Current bag: {bag}')

        if quantity > 0:
            bag[str(item_id)] = quantity
            messages.success(request, f'Updated {event.title} quantity to {bag[str(item_id)]}')
        else:
            bag.pop(str(item_id), None)  
            messages.success(request, f'Removed {event.title} from your bag')

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    else:
        messages.error(request, 'Invalid request method.')
        return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        event = get_object_or_404(Event, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(str(item_id), None)  
        messages.success(request, f'Removed {event.title} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
