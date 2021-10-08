from django.http import request
from django.test import TestCase
from .models import Student
import datetime
from django.urls import reverse

# Create your tests here.

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student =  Student(first_name="Juliet",
                                last_name="AkiraChix",
                                age=22,email="lovie@gmail.com",
                                id_number="74129862",
                                date_of_birth="2000-10-03")

    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_year_of_birth(self):
        current_year = datetime.datetime.now().year
        year = current_year - self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_student_registration_view(self):
        url = reverse("registerStudent")
        data = {"first_name":self.student.first_name,
                "last_name": self.student.last_name,
                "age": self.student.age,
                "id_number":self.student.id_number,
                "date_of_birth":self.student.date_of_birth}

        request = self.client.post(url,data)
        self.assertEqual(request.status_code,200)
       
