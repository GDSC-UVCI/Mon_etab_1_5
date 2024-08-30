from django import forms
from .models import UserModel

class UserAddForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['id', 'created_at']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }