from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .forms import CheckoutForm


def checkout(request):
    Customer = request.Customer
    form = CheckoutForm()  # Khởi tạo form (chỉ để hiển thị)
    return render(request, 'checkout.html', {'form': form}, {'Customer': Customer})

>>>>>>> 79d543bf3bc5205beea91efbda29ac9998cb5c6d
