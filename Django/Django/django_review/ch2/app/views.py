from django.shortcuts import render
from .forms import Registration

def registration(req):
    if req.method == "POST":
        print(req.POST['name'])
        print(req.POST['email'])
    else:
        form = Registration()
    return render(req , 'register.html', {"register":form})