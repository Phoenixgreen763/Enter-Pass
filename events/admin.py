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
        'price',
    )

    ordering = ('date',)
    search_fields = ('title', 'description', 'location')
    list_filter = ('category', 'date')

    def display_category(self, obj):
        return obj.category.name  # Fetch the name from the related Category model
    display_category.short_description = 'Category'
    display_category.admin_order_field = 'category'

    def is_sold_out(self, obj):
        """Returns True if the event is sold out, False otherwise."""
        return obj.is_sold_out()
    is_sold_out.boolean = True  

admin.site.register(Event, EventAdmin)

