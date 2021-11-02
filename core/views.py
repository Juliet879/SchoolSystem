from django.shortcuts import render
from landing.decorators import allowed_users




# Create your views here.
@allowed_users(allowed_roles=['admin','students'])

def navbar(request):
    return render(request,'base.html',{})


