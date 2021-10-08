from django import forms
from django.forms import fields
from django.utils.regex_helper import Choice
from .models import Trainer

class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
        widgets = {
            "first_name":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "second_name":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "company":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "course":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "gender_choice":forms.Select(attrs={'class':"form-control",'style':"width:90%"}),
            # "email":forms.EmailInput(attrs={'class':"form-control",'style':"width:90%"}),
            "city":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "resume":forms.FileInput(attrs={'class':"form-control",'style':"width:90%"}),
            "profile_image":forms.FileInput(attrs={'class':"form-control",'style':"width:90%"}),
            "contract":forms.FileInput(attrs={'class':"form-control",'style':"width:90%"}),

        }