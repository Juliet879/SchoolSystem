from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import StudentViewSet,TrainerViewSet,EventViewSet,CourseViewSet



router = routers.DefaultRouter()
router.register("students/", StudentViewSet)
router.register("trainers/", TrainerViewSet)
router.register("courses/", CourseViewSet)
router.register("events/", EventViewSet)



urlpatterns = [
    path("",include(router.urls))
]