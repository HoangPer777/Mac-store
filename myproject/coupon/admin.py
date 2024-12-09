from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'maxValue', 'from_date', 'to_date', 'active', 'remaining', 'type', 'amount', 'sku')
    list_filter = ('active', 'type')
    search_fields = ('code', 'sku')
    ordering = ('-from_date',)

# Đăng ký model và class quản lý
admin.site.register(Coupon, CouponAdmin)
