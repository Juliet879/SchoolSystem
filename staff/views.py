from .forms import StaffRegistrationForm
from django.shortcuts import render,redirect
from .models import Staff
from landing.decorators import allowed_users


# Create your views here.
@allowed_users(allowed_roles=['admin'])
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

@allowed_users(allowed_roles=['admin','trainers','staff'])
def staff_list(request):
    staffs = Staff.objects.all()
    return render(request,"staff_list.html",{"staffs":staffs})

@allowed_users(allowed_roles=['admin','staff'])
def edit_staff(request,id):
    staff = Staff.objects.get(id=id)
    if request.method =="POST":
        form = StaffRegistrationForm(request.POST,request.FILES,instance=staff)
        if form.is_valid():
            form.save()
    else:
        form = StaffRegistrationForm(instance=staff)
    return render(request,"edit_staff.html",{"form":form})

@allowed_users(allowed_roles=['admin'])
def staff_profile(request,id):
    staff = Staff.objects.get(id=id)
    return render(request,"staff_profile.html",{"staff":staff})

@allowed_users(allowed_roles=['admin'])
def delete_staff(request,id):
    try:
        staff = Staff.objects.get(id=id)
        staff.delete()
    except Staff.DoesNotExist:
        staff = None

    return redirect(staff_list)