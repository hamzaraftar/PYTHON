from django.shortcuts import render
from .forms import StudentForm

def show_form_data (request):
    if request.method == "POST":    
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['email'])
    else:
        fm = StudentForm()  

    return render(request , 'student/register.html',{'form':fm})
