from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location',
                  'total_tickets', 'available_tickets',
                  'price', 'category']
