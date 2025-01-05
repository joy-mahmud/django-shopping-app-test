from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))


class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
        #         'placeholder': 'Username'
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
        #         'placeholder': 'Password'
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #         'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500',
        #         'placeholder': 'Confirm Password'
        #     }),
        # }