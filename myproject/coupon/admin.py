from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):

    list_display = ('code', 'type', 'maxValue','percent','amount' ,'from_date', 'to_date', 'active', 'remaining')
    list_filter = ('active', 'from_date', 'to_date')
    search_fields = ('code',)
    ordering = ('-from_date',)


