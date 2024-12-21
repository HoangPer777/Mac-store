from g_admin import views
from django.urls import path

app_name = 'g_admin'

urlpatterns = [
    path('', views.get_admin, name='g_admin'),

    path('product/add', views.creatProduct, name='creatProduct'),
    path('list/', views.admin_get_product, name='admin_get_product'),
]