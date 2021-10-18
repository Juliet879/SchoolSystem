from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets= {
            "username":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "email":forms.EmailInput(attrs={'class':"form-control",'style':"width:95%"}),
            "password1":forms.PasswordInput(attrs={'class':"form-control",'style':"width:95%"}),
            "password2":forms.PasswordInput(attrs={'class':"form-control",'style':"width:95%"}),
        }