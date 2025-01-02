from django import forms
from .models import User

class UserForm(forms.ModelForm):

    gender = forms.ChoiceField(
        choices=[
            ('M', 'Nam'),
            ('F', 'Nữ'),
            ('O', 'Khác'),
        ],
        widget=forms.Select(attrs={
            'class': 'input_form',
        }),
        label="Giới tính",
    )

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

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'input_form',
                'placeholder': 'Nhập họ và tên',
            }),
            'display_name': forms.TextInput(attrs={
                'class': 'input_form',
                'placeholder': 'Nhập tên tài khoản',
            }),
            'birth': forms.DateInput(attrs={
                'class': 'input_form',
                'type': 'date',
            }),
            'gender': forms.Select(attrs={
                'class': 'input_form gender_form',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input_form',
                'placeholder': 'Nhập email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'input_form',
                'placeholder': 'Nhập số điện thoại',
            }),
        }
