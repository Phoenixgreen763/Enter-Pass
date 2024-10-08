from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percentage', 'expiration_date', 'usage_limit', 'used_count')
    search_fields = ('code',)

admin.site.register(Coupon, CouponAdmin)