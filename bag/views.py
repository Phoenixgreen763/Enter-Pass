from decimal import Decimal
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from events.models import Event  
from coupons.views import apply_coupon


def view_bag(request):
    if request.method == 'POST':
        return apply_coupon(request) 
    
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    bag_items = []
    total = Decimal('0.00')  # Initialize total as Decimal

    for item_id, quantity in bag.items():
        try:
            event = Event.objects.get(pk=item_id)  # Fetch the event by ID
            subtotal = event.price * quantity  # Calculate subtotal for this item
            
            if isinstance(subtotal, float):
                subtotal = Decimal(subtotal)

            total += subtotal  
            
            bag_items.append({
                'event': event,
                'quantity': quantity,
                'subtotal': subtotal,
                'item_id': item_id
            })
        except Event.DoesNotExist:
            messages.error(request, f'Event with ID {item_id} does not exist.')

    # Retrieve discount code and amount from session
    discount_code = request.session.get('discount_code', '')  
    discount_percentage = request.session.get('discount_percentage', Decimal('0.00'))

    if isinstance(discount_percentage, float):
        discount_percentage = Decimal(discount_percentage)

    # Calculate the discount amount
    discount_amount = (discount_percentage / Decimal('100')) * total  # Convert percentage to decimal
    grand_total = total - discount_amount 

    context = {
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
        'messages': messages.get_messages(request), 
        'discount_code': discount_code,
    }

    return render(request, 'bag/bag.html', context)

def add_to_bag(request, item_id):
    """ Add a quantity of the specified event to the shopping bag """
    if request.method == "POST":
        event = get_object_or_404(Event, pk=item_id)

        # Ensure quantity and redirect_url are set in the POST data
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not specified
        redirect_url = request.POST.get('redirect_url', reverse('view_bag'))  # Default redirect

        # Initialize bag
        bag = request.session.get('bag', {})
        
        print(f'Adding item ID {item_id} to the bag. Quantity: {quantity}. Current bag: {bag}')

        # Check if the item already exists in the bag
        if str(item_id) in bag.keys():  # Make sure to convert item_id to string  
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
    """ Adjust the quantity of the specified event """
    if request.method == "POST":
        event = get_object_or_404(Event, pk=item_id)
        quantity = int(request.POST.get('quantity', 0))  # Default to 0 if not specified
        bag = request.session.get('bag', {})

        print(f'Adjusting item ID {item_id}. New Quantity: {quantity}. Current bag: {bag}')

        if quantity > 0:
            bag[str(item_id)] = quantity
            messages.success(request, f'Updated {event.title} quantity to {bag[str(item_id)]}')
        else:
            bag.pop(str(item_id), None)  # Use None to avoid KeyError if not in bag
            messages.success(request, f'Removed {event.title} from your bag')

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    else:
        messages.error(request, 'Invalid request method.')
        return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """
    try:
        event = get_object_or_404(Event, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(str(item_id), None)  # Safely remove item
        messages.success(request, f'Removed {event.title} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
    
def calculate_grand_total(bag, discount_percentage=Decimal('0.00')):
    """Calculate the grand total of the items in the bag, applying a percentage discount."""
    total = Decimal('0.00')  

    for item_id, quantity in bag.items():
        try:
            event = Event.objects.get(pk=item_id)
            subtotal = event.price * quantity  
            total += subtotal
        except Event.DoesNotExist:
            continue  

    # Ensure discount_percentage is treated as a Decimal
    if isinstance(discount_percentage, float):
        discount_percentage = Decimal(discount_percentage)

    # Calculate the discount amount based on the percentage
    if discount_percentage > Decimal('0.00'):
        discount_amount = (discount_percentage / Decimal('100')) * total
        grand_total = total - discount_amount
    else:
        grand_total = total 

    # Ensure grand total does not go below zero
    if grand_total < Decimal('0.00'):
        grand_total = Decimal('0.00')

    return grand_total