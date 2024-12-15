from django.shortcuts import render
from user.models import User

def checkout(request):
    form = CheckoutForm()  
    return render(request, 'checkout.html', {'form': form})

def profile_view(request):
    user = request.user  
    return render(request, 'user/profile.html', {'user': user})



