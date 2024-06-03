from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegisterUserModel


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = RegisterUserModel
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', min_length=3, max_length=50)
    password = forms.CharField(label='Password', min_length=8, max_length=50)

    class Meta:
        model = UserCreationForm
        fields = ('username', 'password')
