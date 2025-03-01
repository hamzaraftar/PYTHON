from django.shortcuts import render
from student.forms import Registeration

# Create your views here.
def register_student(req):
    fm = Registeration()
    return render(req, 'student/register.html' , {'form':fm})