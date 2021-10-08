from django import forms
from django.utils.regex_helper import Choice
from .models import Event


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Event
        # tells the database it wants all the data in the database for chosen fields you put the fields in a tuple
        fields = "__all__"   
        widgets= {
            "event_name":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "organizer":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "guest":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "date":forms.DateInput(attrs={'class':"form-control",'style':"width:95%"}),
            "event_description":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
            "start_time":forms.DateTimeInput(attrs={'class':"form-control",'style':"width:95%",'type':'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            "end_time":forms.DateTimeInput(attrs={'class':"form-control",'style':"width:95%",'type':'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            "event_link":forms.TextInput(attrs={'class':"form-control",'style':"width:95%"}),
        }

    def __init__(self,*args,**kwargs):
        super(EventRegistrationForm,self).__init__(*args,**kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

    