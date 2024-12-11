from django.urls import path

from cart.views import cart_add, cart_detail
from . import views
from .views import product_list

app_name = 'product'

urlpatterns = [
    path('create/', views.product_create, name='product_create'),
    path('list/', product_list, name='product_list'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('detail/', cart_detail, name='cart_detail'),
]
