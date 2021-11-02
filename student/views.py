from django.shortcuts import redirect, render
from .forms import StudentRegistrationForm
from .models import Student
from landing.decorators import allowed_users

# from django.http import JsonResponse
# from django.core import serializers
# from django.core.files.storage import FileSystemStorage

#Register a new student.
@allowed_users(allowed_roles=['admin','students'])
def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = StudentRegistrationForm()
    return render(request ,"register_student.html",{"form":form})


#Displaying a list of the student
@allowed_users(allowed_roles=['admin','students','trainers'])
def student_list(request):
    students = Student.objects.all()
    return render(request,"student_list.html",{"students":students})

#editing a student
@allowed_users(allowed_roles=['admin','students'])
def edit_student(request,id):
    student = Student.objects.get(id=id)
    if request.method =="POST":
        form = StudentRegistrationForm(request.POST,instance=student)
        if form.is_valid():
            form.save()

    else:
        form = StudentRegistrationForm(instance=student)
    return render(request,'edit_student.html',{"form":form})

#single instance view
@allowed_users(allowed_roles=['admin','students','trainers'])
def student_profile(request,id):
    student = Student.objects.get(id=id)
    return render(request,'student_profile.html',{"student":student})


#delete a student
@allowed_users(allowed_roles=['admin'])
def delete_student(request,id):
    try:
        student = Student.objects.get(id=id)
        student.delete()
        
    except Student.DoesNotExist:
        student = None

    return redirect(student_list)



# def dashboard_pivot(request):
#     return render(request,'dashboard.html',{})


# def pivot_data(request):
#     dataset = Student.objects.all()
#     data = serializers.serialize('json',dataset)
#     return JsonResponse(data,safe=False)