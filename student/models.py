from django.db import models
import datetime
# from phonenumber_fields.modelfields import PhoneNumberField

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    age = models.PositiveSmallIntegerField()
    date_of_birth =  models.DateField()
    nations = [
            ("Kenyan","Kenyan"),
            ("Rwandan","Rwandan"),
            ("Ugandan","Ugandan"),
            ("South Sudaneese","South Sudaneese"),
    ]
    nationality = models.CharField(max_length=15,choices=nations,default="Kenyan")
    classes = [
        ("LOVELACE","Lovelace"),
        ("ANITA_B","AnitaB"),
        ("LISALAB","LisaLab"),
    ]
    class_name = models.CharField(max_length=10,choices=classes,default="AnitaB",null=True,blank=True)
    id_number = models.CharField(max_length=20)
    email = models.EmailField()
    academic_year = models.IntegerField(null=True,blank=True)
    medical_report = models.FileField(upload_to="documents/")
    guardian_name = models.CharField(max_length=25)
    # guardian_contact = models.
    profile_image = models.ImageField(upload_to ="images/",null=True,blank=True)
    
    
    def full_name(self):
        return f"{self.full_name} {self.last_name}"

    def year_of_birth(self):
        current_year = datetime.datetime.now().year
        return current_year - self.age
    
