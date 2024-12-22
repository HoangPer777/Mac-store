from django.urls import path
from . import views



app_name='coupon'
urlpatterns = [
    path('create/', views.create_coupon, name='create_coupon'),
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),
]
