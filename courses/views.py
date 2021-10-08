from django.shortcuts import render
from .forms import CourseRegistrationForm
from .models import Course

# Create your views here.
def add_course(request):
    if request.method == "POST":
        form = CourseRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = CourseRegistrationForm()
    return render(request,'course.html',{"form":form})
    
def course_list(request):
    courses = Course.objects.all()
    return render(request, "course_list.html",{"courses":courses})

def edit_course(request,id):
    course = Course.objects.get(id=id)
    if request.method =="POST":
        form = CourseRegistrationForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()
    else:
        form = CourseRegistrationForm(instance=course)
    return render(request,"edit_course.html",{"form":form})