from django.shortcuts import redirect, render
from student.models import Student
from trainer.models import Trainer
from courses.models import Course
from staff.models import Staff
from landing.decorators import allowed_users
# from .models import Order
# from django.http import JsonResponse
# from django.core import serializers

# Create your views here.
# def dashboard_pivot(request):
#     return render(request,'dashboard.html',{})


# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json',dataset)

@allowed_users(allowed_roles=['admin','students','trainers'])
def home(request):
# Authentication
    # if request.user.is_authenticated:
    students = Student.objects.count()
    trainers = Trainer.objects.count()    
    staffs = Staff.objects.count()
    courses = Course.objects.count()

    data = {"students":students,"trainers":trainers,"courses":courses,"staffs":staffs}
    return render(request,"dashboard.html",data)

    # else:
    #     return redirect("auth_login")
