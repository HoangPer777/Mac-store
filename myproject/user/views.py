from django.shortcuts import render, redirect
from .forms import UserForm
from address.forms import AddressForm

def user_info(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        address_form = AddressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()
            return redirect('success')  # Điều hướng đến trang thành công
    else:
        user_form = UserForm()
        address_form = AddressForm()

    return render(request, 'user_info.html', {
        'user_form': user_form,
        'address_form': address_form
    })
