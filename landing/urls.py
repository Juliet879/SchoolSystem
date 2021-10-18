from django.urls import path
from .views import index,login_user,register,log_out_user


urlpatterns = [
    path("",index,name="index"),
    path("login",login_user,name="login"),
    path("logout",log_out_user,name="logout"),
    path("register",register,name="register"),


]