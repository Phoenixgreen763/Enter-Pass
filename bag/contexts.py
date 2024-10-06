from decimal import Decimal
from django.shortcuts import get_object_or_404
from events.models import Event

def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    event_count = 0
    bag = request.session.get('bag', {})

    # Get the discount and coupon code from the session, defaulting to 0 if not set
    discount = request.session.get('discount', 0)
    coupon_code = request.session.get('coupon_code', None)

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            # Single quantity for this item
            event = get_object_or_404(Event, pk=item_id)
            total += item_data * event.price
            event_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'event': event,
            })
        else:
            # Handling items with size variations
            event = get_object_or_404(Event, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * event.price
                event_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'event': event,
                    'size': size,
                })

    # Calculate the discount amount and grand total
    discount_amount = total * Decimal(discount) if discount else Decimal('0.00')
    grand_total = total - discount_amount

    context = {
        'bag_items': bag_items,
        'total': total,
        'event_count': event_count,
        'discount_amount': discount_amount,
        'grand_total': grand_total,
        'coupon_code': coupon_code,  # Pass the coupon code if applied
    }

    return context
