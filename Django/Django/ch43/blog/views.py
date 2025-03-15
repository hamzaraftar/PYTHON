from django.shortcuts import render
from .models import Student

def home(request):
    student_data = Student.student.all()
    return render(request , 'home.html',{ "studetn_data":student_data  })
