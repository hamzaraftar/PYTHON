from django.shortcuts import render
from .forms import StudentForms

def registrations(req):
    fm = StudentForms()
    return render(req ,  'student/register.html'  ,{"form":fm})

