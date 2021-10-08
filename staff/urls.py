from django.urls import path
from .views import staff_register,staff_list,edit_staff,staff_profile,delete_staff



urlpatterns = [
    path("register_staff",staff_register,name="staffRegister"),
    path('staff_list',staff_list,name="staffList"),
    path('edit/<int:id>/',edit_staff, name="editStaff"),
    path('profile/<int:id>/',staff_profile,name="staffProfile"),
    path('delete/<int:id>/',delete_staff,name="deleteStuff"),
]