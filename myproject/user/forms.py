from django import forms
from .models import User

class UserForm(forms.ModelForm):
    # class Meta:
    #     model = User
    #     fields = ['full_name', 'display_name', 'birth', 'gender', 'email', 'phone']

    class Meta:
        model = User
        fields = ['full_name', 'display_name', 'birth', 'gender', 'email', 'phone']
        labels = {
            'full_name': 'Họ và tên',
            'display_name': 'Tên tài khoản',
            'birth': 'Ngày sinh',
            'gender': 'Giới tính',
            'email': 'Email',
            'phone': 'Số điện thoại',
        }