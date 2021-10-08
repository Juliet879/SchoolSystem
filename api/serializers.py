from django.db import models
from django.db.models import fields
from rest_framework import serializers, viewsets
from student.models import Student
from trainer.models import Trainer
from courses.models import Course
from myCalendar.models import Event


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("first_name","last_name","age","class_name","nationality","email")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ("first_name","last_name","company","email","course")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("course_name","course_trainer","course_description")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("event_name","organizer","start_time","end_time","event_link")
