from django.shortcuts import render
from .forms import CheckoutForm
from user.models import User

def checkout(request):
    form = CheckoutForm()  # Khởi tạo form (chỉ để hiển thị)
    return render(request, 'checkout.html', {'form': form})

def profile_view(request):
    user = request.user  
    return render(request, 'user/profile.html', {'user': user})



