from g_admin import views
from django.urls import path
urlpatterns = [
    path('', views.get_admin, name='g_admin'),
]