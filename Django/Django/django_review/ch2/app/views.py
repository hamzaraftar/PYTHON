from django.shortcuts import render
from .forms import Registration


def registration(req):
    form = Registration
    return render(req , 'register.html', {"register":form})