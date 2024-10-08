# Generated by Django 5.1.1 on 2024-10-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='discount_amount',
        ),
        migrations.AddField(
            model_name='coupon',
            name='discount_percentage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
