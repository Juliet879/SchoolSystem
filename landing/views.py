from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,"index.html",{})

def login_user(request):
    # if request.user.is_authenticated:
    #     return render(request,'dashboard.html',{})
    # else:
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

def register(request):
    # if request.user.is_authenticated:
    #     return render(request,'dashboard.html',{})
    # else:
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account created successfully for" + user)
            return redirect('login')

    content = {"form":form}
    return render(request,'register.html',content )