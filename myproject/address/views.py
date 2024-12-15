from django.shortcuts import render
from .forms import AddressForm
# Create your views here.
def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        return render(request, 'addressForm.html', {'form': form})
    else:
        form = AddressForm()
    return render(request, 'addressForm.html', {'form': form})  # Xử lý khi request là GET