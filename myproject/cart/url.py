from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('clear/', views.cart_clear, name='cart_clear'),
    path('update-quantity/', views.update_quantity, name='update_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),
    path('checkout/pay/', views.process_payment, name='process_payment'),
    path('total-items/', views.total_items_in_cart, name='total_items_in_cart'),
    path('cart/thank-you/', views.thank_you, name='thank_you'),
#     path('checkout_buy_now/', views.checkout_view, name='checkout_view'),
    path('checkout/buy_now/', views.checkout_buy_now, name='checkout_buy_now'),
#     path('checkout/buy_now/', views.checkout_buy_now, name='checkout_buy_now'),
]
