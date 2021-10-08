from django import forms
from django.forms import fields
from django.utils.regex_helper import Choice
from .models import Staff

class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"
        widgets = {
            "first_name":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "second_name":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "role":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "gender_choice":forms.Select(attrs={'class':"form-control",'style':"width:90%"}),
            "city":forms.TextInput(attrs={'class':"form-control",'style':"width:90%"}),
            "resume":forms.FileInput(attrs={'class':"form-control",'style':"width:90%"}),
            "profile_image":forms.FileInput(attrs={'class':"form-control",'style':"width:90%"}),
            "contract":forms.FileInput(attrs={'class':"form-control",'style':"width:90%"}),

        }