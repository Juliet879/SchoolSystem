from django.urls import path
from .views import trainer_register,trainer_list,edit_trainer,trainer_profile,delete_trainer


urlpatterns =[
    path('register',trainer_register,name="registerTrainer"),
    path('trainer_list',trainer_list,name="trainerList"),
    path('edit/<int:id>/',edit_trainer,name="editTrainer"),
    path('profile/<int:id>/',trainer_profile,name="trainerProfile"),
    path('delete/<int:id>/',delete_trainer,name="deleteTrainer"),
]