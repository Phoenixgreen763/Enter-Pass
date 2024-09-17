# events/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the root URL of the 'events' app to the 'index' view
    # Add more URL patterns here as needed
]
