from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=40)
    course_trainer = models.CharField(max_length=35)
    course_code = models.CharField(max_length=10)
    course_description = models.TextField(max_length=200)
    notes = models.FileField(upload_to="Documents")
    course_structure = models.FileField(upload_to="Documents")
