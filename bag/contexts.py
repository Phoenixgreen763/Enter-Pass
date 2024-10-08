from decimal import Decimal
from django.shortcuts import get_object_or_404
from events.models import Event

def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    event_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):  
            event = get_object_or_404(Event, pk=item_id)
            total += item_data * event.price 
            event_count += item_data  
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'event': event,
            })

    # Retrieve the discount amount from the session (if applied)
    discount_amount = request.session.get('discount_amount', Decimal('0.00'))

    if isinstance(discount_amount, float):
        discount_amount = Decimal(discount_amount)

    grand_total = total - discount_amount

    context = {
        'bag_items': bag_items,
        'total': total,
        'event_count': event_count,
        'discount_amount': discount_amount, 
        'grand_total': grand_total,  
    }

    return context