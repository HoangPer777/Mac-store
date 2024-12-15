from django.shortcuts import render
from .forms import CheckoutForm


def checkout(request):
    Customer = request.Customer
    form = CheckoutForm()  # Khởi tạo form (chỉ để hiển thị)
    return render(request, 'checkout.html', {'form': form}, {'Customer': Customer})

