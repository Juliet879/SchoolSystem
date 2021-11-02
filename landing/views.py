from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import Group
from .decorators import allowed_users,unauthenticated_user
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def index(request):
    return render(request,"index.html",{})

@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username, password= password)
        if user is not None:
            login(request,user)
            return render(request,'dashboard.html',{})
        else:
            messages.info(request,'Username OR Password is incorrect')
    content = {}
    return render(request,'login.html',content )

def log_out_user(request):
    logout(request)
    return redirect('login')

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user =form.save()

            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='students')
            user.groups.add(group)
 
            messages.success(request,"Account created successfully for" + username)
            return redirect('login')

    content = {"form":form}
    return render(request,'register.html',content)