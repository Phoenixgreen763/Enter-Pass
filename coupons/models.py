from django.db import models
from django.utils import timezone


class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField()
    usage_limit = models.PositiveIntegerField(default=1)
    used_count = models.PositiveIntegerField(default=0)

    def is_valid(self):
        return (
            self.expiration_date > timezone.now() and
            self.used_count < self.usage_limit
        )

    def __str__(self):
        return self.code
