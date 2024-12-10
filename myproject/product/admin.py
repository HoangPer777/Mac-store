
# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'available', 'created', 'updated', 'vendor', 'collections')
    search_fields = ('name', 'vendor', 'collections', 'tags')
    list_filter = ('available', 'created', 'updated', 'vendor')
    prepopulated_fields = {'slug': ('name',)}  # Tự động tạo slug từ trường name
    ordering = ('name',)
