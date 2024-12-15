from django.contrib import admin

from user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth', 'gender', 'email', 'phone', 'view_detail')  # Thêm view_detail
    search_fields = ('id', 'full_name', 'email', 'phone')
    ordering = ('-id',)
    fields = ('full_name', 'email', 'birth', 'gender', 'phone',)

    def view_detail(self, obj):
        # Tạo liên kết tùy chỉnh đến trang chi tiết
        from django.utils.html import format_html
        return format_html('<a href="/admin/user/user/{}/change/">Xem chi tiết</a>', obj.id)

    view_detail.short_description = 'Chi tiết'

