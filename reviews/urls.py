from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('add/', views.add_review, name='add_review'),
    path('reviews/delete/<int:review_id>/', views.delete_review,
         name='delete_review'),
]
