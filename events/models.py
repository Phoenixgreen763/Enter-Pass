from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('music', 'Music/Festivals'),
        ('theatre', 'Theatre'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    total_tickets = models.PositiveIntegerField()
    available_tickets = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

    def is_sold_out(self):
        """Returns True if the event is sold out."""
        return self.available_tickets == 0
