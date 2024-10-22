from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Coupon


def create_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        discount_percentage = request.POST.get('discount_percentage')
        expiration_date = request.POST.get('expiration_date')
        usage_limit = request.POST.get('usage_limit', 1)

        coupon = Coupon.objects.create(
            code=code,
            discount_percentage=discount_percentage,
            expiration_date=expiration_date,
            usage_limit=usage_limit
        )

        messages.success(
            request,
            f'Coupon {coupon.code} created successfully!'
        )

        return redirect('view_bag')  # Redirect or render a template

    return render(request, 'create_coupon.html')


def apply_coupon(request):
    if request.method == 'POST':
        code = request.POST.get('discount_code')

        try:
            coupon = Coupon.objects.get(code=code)
        except Coupon.DoesNotExist:
            messages.error(request, 'Coupon is invalid or expired.')
            return redirect('view_bag')  # Redirect back to the bag page

        # Validate coupon
        # Make sure you have this method defined in your Coupon model
        if not coupon.is_valid():
            messages.error(request, 'Coupon is invalid or expired.')
            return redirect('view_bag')

        # Update coupon usage count
        coupon.used_count += 1
        coupon.save()

        # Store discount information in the session
        request.session['discount_code'] = coupon.code
        # Convert Decimal to float
        request.session['discount_percentage'] = (
            float(coupon.discount_percentage)
        )

        messages.success(
            request,
            (
                f'Coupon {coupon.code} applied! '
                f'Discount: {coupon.discount_percentage}%'
            )
        )
        return redirect('view_bag')

    # If not a POST request, redirect back
    return redirect('view_bag')


def remove_coupon(request):
    if request.method == 'POST':
        # Clear the discount code and amount from the session
        if 'discount_code' in request.session:
            del request.session['discount_code']
        if 'discount_percentage' in request.session:
            del request.session['discount_percentage']

        messages.success(request, 'Discount code removed.')

    return redirect('view_bag')
