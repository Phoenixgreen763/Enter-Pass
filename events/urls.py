from django.urls import path
from . import views

urlpatterns = [
    path('all-events/', views.all_events, name='all_events'),
]
