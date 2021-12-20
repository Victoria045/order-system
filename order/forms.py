from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer,Product

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image','name', 'price', 'digital',)