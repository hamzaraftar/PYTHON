from django.shortcuts import render
from  django.contrib.auth.forms import UserCreationForm

def sign_up(req):
    if req.method == "POST":   
        fm = UserCreationForm(req.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()
    return render(req , 'signup.html',{"form":fm})