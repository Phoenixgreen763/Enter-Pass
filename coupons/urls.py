# coupons/urls.py
from django.urls import path
from .views import create_coupon, apply_coupon, remove_coupon

urlpatterns = [
    path('create/', create_coupon, name='create_coupon'),
    path('apply/', apply_coupon, name='apply_coupon'),
    path('remove-coupon/', remove_coupon, name='remove_coupon'),
]
