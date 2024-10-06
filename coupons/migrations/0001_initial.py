# Generated by Django 5.1.1 on 2024-10-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expiration_date', models.DateTimeField()),
                ('usage_limit', models.PositiveIntegerField(default=1)),
                ('used_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]