from .views import calculate_grand_total
from decimal import Decimal


def bag_context_processor(request):
    """Context processor to add bag total to all templates."""
    bag = request.session.get('bag', {})
    discount_percentage = request.session.get('discount_percentage',
                                              Decimal('0.00'))
    grand_total = calculate_grand_total(bag, discount_percentage)

    return {
        'grand_total': grand_total,
    }
