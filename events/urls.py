from django.urls import path
from . import views
from .views import edit_event

urlpatterns = [
    path('', views.all_events, name='all_events'),  # All events page
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),  # Event detail page
    path('add/', views.add_event, name='add_event'),
    path('events/edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
]
