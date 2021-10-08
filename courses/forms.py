from django import forms
from .models import Course

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            "course_name":forms.TextInput(attrs = {'class':"forms-counter",'style':"width:90%"}),
            "course_trainer":forms.TextInput(attrs = {'class':"forms-counter",'style':"width:90%"}),
            "course_code":forms.TextInput(attrs = {'class':"forms-counter",'style':"width:90%"}),
            "course_description":forms.TextInput(attrs = {'class':"forms-counter",'style':"width:90%"}),
            "notes":forms.FileInput(attrs = {'class':"forms-counter",'style':"width:90%"}),
            "course_structure":forms.FileInput(attrs = {'class':"forms-counter",'style':"width:90%"})

        }
