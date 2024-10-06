from decimal import Decimal
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from rest_framework import status
from rest_framework.response import Response
from .models import Coupon


def create_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        discount_amount = request.POST.get('discount_amount')
        expiration_date = request.POST.get('expiration_date')
        usage_limit = request.POST.get('usage_limit', 1)

        coupon = Coupon.objects.create(
            code=code,
            discount_amount=discount_amount,
            expiration_date=expiration_date,
            usage_limit=usage_limit
        )
        
        messages.success(request, f'Coupon {coupon.code} created successfully!')
        return redirect('view_bag')  # Redirect or render a template

    return render(request, 'create_coupon.html')

def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('discount_code')  
        
        try:
            coupon = Coupon.objects.get(code=code)  
        except Coupon.DoesNotExist:
            messages.error(request, 'Coupon is invalid or expired.')
            return redirect('view_bag')  

        # Validate coupon
        if not coupon.is_valid():  # Make sure you have this method defined in your Coupon model
            messages.error(request, 'Coupon is invalid or expired.')
            return redirect('view_bag')  

        # Update coupon usage count
        coupon.used_count += 1
        coupon.save()

        request.session['discount_code'] = coupon.code
        request.session['discount_amount'] = coupon.discount_amount

        messages.success(request, f'Coupon {coupon.code} applied! Discount: ${coupon.discount_amount}')
        return redirect('view_bag')  # Redirect back to the bag page

    # If not a POST request, redirect back
    return redirect('view_bag')

def remove_coupon(request):
    if request.method == 'POST':
        # Clear the discount code and amount from the session
        if 'discount_code' in request.session:
            del request.session['discount_code']
        if 'discount_amount' in request.session:
            del request.session['discount_amount']
        
        messages.success(request, 'Discount code removed.')
    
    # Redirect back to the bag page
    return redirect('view_bag')