from .views import calculate_grand_total

def bag_context_processor(request):
    """Context processor to add bag total to all templates."""
    bag = request.session.get('bag', {})
    grand_total = calculate_grand_total(bag)
    return {
        'grand_total': grand_total,
    }
