from django import forms
from .models import Coupon


class CouponApplyForm(forms.Form):

    code = forms.CharField(label="Coupon code", max_length=10)
    original_price = forms.DecimalField(label="Original price", max_digits=10, decimal_places=2)

class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ['code', 'type', 'percent', 'amount', 'maxValue', 'from_date', 'to_date', 'active','remaining']