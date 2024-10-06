from django.urls import path
from . import views
from .views import create_coupon, apply_coupon

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:item_id>/', views.add_to_bag, name='add_to_bag'),  # Ensure item_id is an integer
    path('adjust/<int:item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<int:item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('create_coupon/', create_coupon, name='create_coupon'),
    path('apply_coupon/', apply_coupon, name='apply_coupon'),
]
