from django.shortcuts import render
from .forms import StudentRegistratoion

def show_form(req):
    fm = StudentRegistratoion()
    return render(req , 'student/home.html' ,{'form':fm})

