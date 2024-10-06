from django.urls import path
from . import views
from .views import create_coupon, apply_coupon


urlpatterns = [
    path('create_coupon/', create_coupon, name='create_coupon'),
    path('apply_coupon/', apply_coupon, name='apply_coupon'),
    ]
