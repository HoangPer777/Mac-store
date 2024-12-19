from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'is_primary')
    readonly_fields = ()

    class Media:
        js = ('style/js/component-js/AddProduct.jsc',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    readonly_fields = ('created', 'updated')
    inlines = [ProductImageInline]
