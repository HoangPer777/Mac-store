from django import forms
from address.models import Address
class AddressForm(forms.ModelForm):
     class Meta:
         model = Address
         fields =['province','district','commune','detail']
         labels = {
             'province':'Tỉnh thành',
             'district':'Huyện',
             'commune':'Xã',
             'detail':'Chi tiết',
         }

         widgets = {
             'province': forms.TextInput(attrs={
                 'class': 'input_form',
                 'placeholder': 'Nhập Tỉnh/Thành phố',
             }),
             'district': forms.TextInput(attrs={
                 'class': 'input_form',
                 'placeholder': 'Nhập huyện/Quận',
             }),
             'commune': forms.TextInput(attrs={
                 'class': 'input_form',
                 'placeholder': 'Nhập Xã/Phường',
             }),
             'detail': forms.TextInput(attrs={
                 'class': 'input_form',
                 'placeholder' : "Nhập ghi chú cụ thể"
             })

         }