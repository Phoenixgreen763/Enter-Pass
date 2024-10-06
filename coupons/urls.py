# coupons/urls.py
from django.urls import path
from .views import create_coupon, apply_coupon

urlpatterns = [
    path('create/', create_coupon, name='create_coupon'),
    path('apply/', apply_coupon, name='apply_coupon'),
]