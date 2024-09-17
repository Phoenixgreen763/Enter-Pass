from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')  # Custom foreign key to User model
    total_tickets = models.PositiveIntegerField()  # Custom field to track ticket capacity
    available_tickets = models.PositiveIntegerField()  # Custom field to track remaining tickets

    def __str__(self):
        return self.title

    def is_sold_out(self):
        """Returns True if the event is sold out."""
        return self.available_tickets == 0
