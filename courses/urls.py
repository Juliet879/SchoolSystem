from django.urls import path
from .views import add_course,course_list,edit_course


urlpatterns = [
    path('add_course/',add_course,name='add_course'),
    path('view_courses/',course_list,name='view_courses'),
    path('edit/<int:id>/',edit_course,name='editCourse')
]