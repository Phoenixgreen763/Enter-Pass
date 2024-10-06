from decimal import Decimal
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from events.models import Event  


def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    bag_items = []
    total = Decimal('0.00')  # Initialize total as Decimal

    for item_id, quantity in bag.items():
        try:
            event = Event.objects.get(pk=item_id)  # Fetch the event by ID
            subtotal = event.price * quantity  # Calculate subtotal for this item
            total += subtotal  # Accumulate total
            bag_items.append({
                'event': event,
                'quantity': quantity,
                'subtotal': subtotal,
                'item_id': item_id
            })
        except Event.DoesNotExist:
            messages.error(request, f'Event with ID {item_id} does not exist.')

    grand_total = total  # Set grand total to total

    context = {
        'bag_items': bag_items,
        'total': total,
        'grand_total': grand_total,
        'messages': messages.get_messages(request), 
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
    
def calculate_grand_total(bag):
    """Calculate the grand total for the shopping bag."""
    total = Decimal('0.00')  # Initialize as Decimal
    for item_id, quantity in bag.items():
        try:
            event = Event.objects.get(pk=item_id)  # Fetch the event by ID
            subtotal = event.price * quantity  # Calculate subtotal for this item
            total += subtotal  # Total is now a Decimal
        except Event.DoesNotExist:
            pass  # Optionally log this error or handle it in some way
    return total