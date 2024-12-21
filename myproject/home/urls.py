# project/urls.py
from django.urls import path, include
from home import views
app_name = 'home'

urlpatterns = [
    path('', views.get_home, name='home' ),
]
