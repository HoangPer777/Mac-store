from g_admin import views
from django.urls import path

app_name = 'g_admin'

urlpatterns = [
    path('', views.get_admin, name='g_admin'),
    path('dashboard/', views.get_dashboard, name='g_admin_dashboard'),
    path('product/list/', views.admin_get_product, name='admin_get_product'),
    path('product/add', views.creatProduct, name='creatProduct'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/remove/<int:product_id>/', views.remove_product, name='remove_product'),
    path('coupon/add', views.createCoupon, name='createCoupon'),
    path('coupon/list/', views.get_coupon_list, name='coupon_list'),
    path('reviews', views.admin_feedback_list, name='get_reviews'),
]
