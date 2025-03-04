from django.shortcuts import render
from .forms import StudentForm

def show_form_data (request):
    if request.method == "POST":    
        fm = StudentForm(request.POST)
        print(fm)
    else:
        fm = StudentForm()  

    return render(request , 'student/register.html',{'form':fm})
