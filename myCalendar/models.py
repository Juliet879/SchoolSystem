import datetime
from django.conf.urls import url
from django.db import models
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=40)
    organizer = models.CharField(max_length=35,null=True,blank=True)
    guest = models.CharField(max_length=35,null=True,blank=True)
    date = models.DateTimeField(max_length=10)
    start_time = models.DateTimeField(default=datetime.date.today)
    end_time =models.DateTimeField()
    event_link = models.CharField(max_length=250,null=True,blank=True)


    @property
    def get_html_url(self):
        url = reverse('myCalendar:editEvent',args=(self.id,))

        return f'<a href="{url}">{self.event_name}</a>'