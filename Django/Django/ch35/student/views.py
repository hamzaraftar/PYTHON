from django.shortcuts import render
from  .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm


def sign_up(req):
    if req.method == "POST":   
        fm = SignUpForm(req.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(req , 'signup.html',{"form":fm})


def log_in(req):
    fm = AuthenticationForm()
    return render(req , 'login.html' , {'form':fm})