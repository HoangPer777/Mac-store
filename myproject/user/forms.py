from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'display_name', 'birth', 'gender', 'email', 'phone']
