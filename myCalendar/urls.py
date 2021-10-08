from django.urls import path
from django.conf.urls import url
from . import views 

app_name = 'myCalendar'
urlpatterns = [
    path("event_list/",views.event_list,name="viewEvent"),
    path("calender/",views.CalendarView.as_view(), name='calendar'),
    path("new/",views.register_event, name="newEvent"),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.register_event, name='editEvent'),
]