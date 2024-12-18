from django.contrib import admin

from .forms import ProductForm
from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'category', 'price', 'stock_quantity', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}  # Nếu có slug
    ordering = ('name',)
    readonly_fields = ('created', 'updated')

    # Tùy chỉnh form để hiển thị ảnh hiện tại nếu có
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            kwargs['widget'] = admin.widgets.AdminFileWidget  # Widget để upload ảnh
        return field
