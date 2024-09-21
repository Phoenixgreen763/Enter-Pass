from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='all_events'),  # All events page
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),  # Event detail page
]
