from .views import calculate_grand_total

def bag_context_processor(request):
    """Context processor to add bag total and discount to all templates."""
    bag = request.session.get('bag', {})

    # Calculate the base grand total without any discounts
    total = calculate_grand_total(bag)
    
    discount = request.session.get('discount', 0)  # Default to 0 if not applied
    coupon_code = request.session.get('coupon_code', None)

    discount_amount = total * discount if discount else 0
    grand_total = total - discount_amount

    return {
        'total': total, 
        'discount_amount': discount_amount,
        'grand_total': grand_total,
        'coupon_code': coupon_code,  # Include coupon code in the context if applied
    }
