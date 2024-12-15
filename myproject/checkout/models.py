from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=255)
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    product_id = forms.IntegerField()
    quantity = forms.IntegerField()
