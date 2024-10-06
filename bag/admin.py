from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_amount', 'expiration_date', 'usage_limit', 'used_count', 'is_valid')
    search_fields = ('code',)

admin.site.register(Coupon, CouponAdmin)