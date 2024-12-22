from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('home/', lambda request: render(request, 'userHome.html'), name='home'),
]
