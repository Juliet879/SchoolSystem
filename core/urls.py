from .views import navbar
from django.urls import path


urlpatterns = [
    path("",navbar,name="myNavbar")
]