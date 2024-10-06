from .views import calculate_grand_total
from decimal import Decimal


def bag_context_processor(request):
    """Context processor to add bag total to all templates."""
    bag = request.session.get('bag', {})
    discount_amount = request.session.get('discount_amount', Decimal('0.00')) 
    grand_total = calculate_grand_total(bag, discount_amount) 
    
    return {
        'grand_total': grand_total,
    }