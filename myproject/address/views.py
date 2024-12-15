from django.shortcuts import render
from .forms import AddressForm
# Create your views here.
def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Chuyển hướng đến trang success
        else:
            return render(request, 'addAddress.html', {'form': form})
    else:
        form = AddressForm()
    return render(request, 'addAddress.html', {'form': form})  # Xử lý khi request là GET
def success(request):
    return render(request, 'success.html')