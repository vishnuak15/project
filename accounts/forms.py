from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name','email','role', 'country', 'nationalitie', 'Mobile', 'password1', 'password2')