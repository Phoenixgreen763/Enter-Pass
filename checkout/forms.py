from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    promo_code = forms.CharField(required=False, max_length=20, label='Promo Code', widget=forms.TextInput(attrs={
        'placeholder': 'Enter promo code',
        'class': 'stripe-style-input',
    }))

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'promo_code',)  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
