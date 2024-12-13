from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'maxValue', 'from_date', 'to_date', 'active', 'remaining', 'sku')
    list_filter = ('active', 'from_date', 'to_date')
    search_fields = ('code', 'sku')
    ordering = ('-from_date',)


