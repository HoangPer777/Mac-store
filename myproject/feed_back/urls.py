from django.urls import path
from .views import save_feedback, classify_feedback, delete_feedback

urlpatterns = [
    path('save/', save_feedback, name='save_feedback'),
    path('classify/', classify_feedback, name='classify_feedback'),
    path('delete/', delete_feedback, name='delete_feedback'),
]
