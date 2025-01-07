from django.shortcuts import render,redirect
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

def index(request):
    feature = Feature.objects.all()
    return render(request, 'index.html',{'features' :feature } )


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email= email).exists():
                messages.info(request , "Email already exist")
                return redirect('/register/')
            
            elif User.objects.filter(username= username).exists():
                messages.info(request , "User name  already in use")
                return redirect('/register/')
            
            else:
                user = User.objects.create_user(username=username , email=email , password=password)
                user.save()
                return redirect('login/')
            
        else:
            messages.info(request , "Password is not same")
            return redirect('/register/')
        
    else:
        return render(request, 'register.html')

def login(request):
    pass