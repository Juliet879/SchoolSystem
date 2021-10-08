from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    company    = models.CharField(max_length=30)
    course   = models.CharField(max_length=30)
    gender_choices   = [
        ('Female','Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),

    ]
    gender = models.CharField(max_length=6,choices=gender_choices,default='')
    joining_date = models.DateField()
    salary = models.BigIntegerField()
    email = models.EmailField(null=True,blank=True)
    city = models.CharField(max_length=12)
    resume = models.FileField(upload_to="documents/")
    contract = models.FileField(upload_to="documents/")
    profile_image = models.ImageField(upload_to ="images/",null=True,blank=True)
