from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()

    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]
        )  # Assuming a 1-5 rating
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} - Rating: {self.rating}'
