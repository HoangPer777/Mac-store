from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_coupon, name='create_coupon'),
   
]
