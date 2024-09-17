from django.urls import path
from . import views

urlpatterns = [
    path('all-events/', views.all_events, name='all_events'),
    path('events/by-price/', views.events_by_price, name='events_by_price'),
    path('events/by-rating/', views.events_by_rating, name='events_by_rating'),
    path('events/category/<str:category>/', views.events_by_category, name='events_by_category'),
    path('events/special/<str:special>/', views.events_special, name='events_special'),
]
