from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'date',
        'location',
        'total_tickets',
        'available_tickets',
        'display_category',
        'is_sold_out',
    )

    ordering = ('date',)
    search_fields = ('title', 'description', 'location')
    list_filter = ('category', 'date')

    def display_category(self, obj):
        return dict(Event.CATEGORY_CHOICES).get(obj.category, obj.category)
    display_category.short_description = 'Category'
    display_category.admin_order_field = 'category'
    
    def is_sold_out(self, obj):
        """Returns True if the event is sold out, False otherwise."""
        return obj.is_sold_out()
    is_sold_out.boolean = True  # This tells Django to render the result as a boolean icon

admin.site.register(Event, EventAdmin)
