from django.shortcuts import render
from .forms import StudentForm

def show_form_data (request):
    if request.method == "POST":    
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            return render(request , 'student/success.html',{'nm':name})

    else:
        fm = StudentForm()  

    return render(request , 'student/register.html',{'form':fm})
