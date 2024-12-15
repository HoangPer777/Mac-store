from django.urls import path
from .views import create_address, success
from django.http import HttpResponse
urlpatterns = [
    path('create-address/',create_address, name='create_address'),
    path('success/', success, name='success'),
]


