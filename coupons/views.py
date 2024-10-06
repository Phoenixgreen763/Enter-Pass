from decimal import Decimal
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from rest_framework import status
from rest_framework.response import Response
from .models import Coupon


def create_coupon(request):
    code = request.data.get('code')
    discount_amount = request.data.get('discount_amount')
    expiration_date = request.data.get('expiration_date')
    usage_limit = request.data.get('usage_limit', 1)

    coupon = Coupon.objects.create(
        code=code,
        discount_amount=discount_amount,
        expiration_date=expiration_date,
        usage_limit=usage_limit
    )
    
    return Response({"id": coupon.id, "code": coupon.code}, status=status.HTTP_201_CREATED)

def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('discount_code')  # Use POST data
        
        # Attempt to get the coupon by code
        coupon = get_object_or_404(Coupon, code=code)

        # Validate coupon
        if not coupon.is_valid():
            messages.error(request, 'Coupon is invalid or expired.')
            return redirect('view_bag')  # Redirect back to the bag page

        # Update coupon usage count
        coupon.used_count += 1
        coupon.save()

        # Store discount information in the session
        request.session['discount_code'] = coupon.code
        request.session['discount_amount'] = coupon.discount_amount

        messages.success(request, f'Coupon {coupon.code} applied! Discount: ${coupon.discount_amount}')
        return redirect('view_bag')  # Redirect back to the bag page

    # If not a POST request, redirect back
    return redirect('view_bag')