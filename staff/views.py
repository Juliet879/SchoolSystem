from .forms import StaffRegistrationForm
from django.shortcuts import render,redirect
from .models import Staff

# Create your views here.
def staff_register(request):
    if request.method == "POST":
        form = StaffRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = StaffRegistrationForm()
    return render(request ,"register_staff.html",{"form":form})

def staff_list(request):
    staffs = Staff.objects.all()
    return render(request,"staff_list.html",{"staffs":staffs})

def edit_staff(request,id):
    staff = Staff.objects.get(id=id)
    if request.method =="POST":
        form = StaffRegistrationForm(request.POST,request.FILES,instance=staff)
        if form.is_valid():
            form.save()
    else:
        form = StaffRegistrationForm(instance=staff)
    return render(request,"edit_staff.html",{"form":form})

def staff_profile(request,id):
    staff = Staff.objects.get(id=id)
    return render(request,"staff_profile.html",{"staff":staff})

def delete_staff(id):
    staff = Staff.objects.get(id=id)
    staff.delete()
    return redirect("staff_list")