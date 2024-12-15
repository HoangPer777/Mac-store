from django.urls import path

from cart.views import cart_add, cart_detail
from . import views
from .views import product_list, product_detail
from django.urls import path, include
app_name = 'product'

urlpatterns = [
    path('create/', views.product_create, name='product_create'),
    path('category/<int:category_id>/', product_list, name='product_list_by_category'),
    path('detail/<int:product_id>', product_detail, name='product_detail'),
    path('cart/', include('cart.url')),
    path('add/<int:product_id>/', cart_add, name='cart_add'),


]
