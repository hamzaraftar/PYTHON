from django.shortcuts import render
from  .forms import SignUpForm

def sign_up(req):
    if req.method == "POST":   
        fm = SignUpForm(req.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(req , 'signup.html',{"form":fm})