<<<<<<< HEAD
from django.shortcuts import render
from .forms import CheckoutForm
from user.models import User

def checkout(request):
    form = CheckoutForm()  # Khởi tạo form (chỉ để hiển thị)
    return render(request, 'checkout.html', {'form': form})

def profile_view(request):
    user = request.user  
    return render(request, 'user/profile.html', {'user': user})



=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
>>>>>>> 79d543bf3bc5205beea91efbda29ac9998cb5c6d
