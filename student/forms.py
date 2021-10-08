from django import forms
from .models import Student


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        # tells the database it wants all the data in the database for chosen fields you put the fields in a tuple
        fields = "__all__"     
        widgets= {
            "first_name":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "last_name":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "age":forms.NumberInput(attrs={'class':"form-control",'style':"width:95%"}),
            "date_of_birth":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "nationality":forms.Select(attrs={'class':"form-control",'style':"width:95%"}),
            "class_name":forms.Select(attrs={'class':"form-control",'style':"width:95%"}),
            "id_number":forms.NumberInput(attrs={'class':"form-control",'style':"width:95%"}),
            "email":forms.EmailInput(attrs={'class':"form-control",'style':"width:95%"}),
            "academic_year":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "guardian_name":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "medical_report":forms.FileInput(attrs={'class':"form-control",'style':"width:95%"}),
            "profile_image":forms.FileInput(attrs={'class':"form-control",'style':"width:95%"})
        }

