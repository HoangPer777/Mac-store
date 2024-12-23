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