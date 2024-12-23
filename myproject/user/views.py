from django.shortcuts import render, redirect
from .forms import UserForm
from address.forms import AddressForm
from .models import User


def user_info(request):
    if not request.user.is_authenticated:
        # Điều hướng nếu người dùng chưa đăng nhập
        return redirect('login')

        # Lấy thông tin của user đang đăng nhập
    user = request.user

    if request.method == 'POST':
        # Lấy dữ liệu từ biểu mẫu
        user_form = UserForm(request.POST, instance=user)
        address_form = AddressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            # Lưu thông tin người dùng
            user_form.save()

            # Lưu thông tin địa chỉ
            address = address_form.save(commit=False)
            address.user = user
            address.save()

            return redirect('success')  # Điều hướng đến trang thành công
    else:
        # Nếu user đã có thông tin, hiển thị trong form
        user_form = UserForm(instance=user)
        address_form = AddressForm()

    return render(request, 'user_info.html', {
        'user_form': user_form,
        'address_form': address_form
    })
