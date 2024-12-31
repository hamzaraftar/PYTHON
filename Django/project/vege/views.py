from django.shortcuts import render,redirect
from .models import Recepie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    if request.method == 'POST':

        data = request.POST 
        image = request.FILES.get('image')
        name = data.get('name')
        description = data.get('description')     

        Recepie.objects.create(
            name=name,
            description=description,
            image=image
        )
    # return redirect('repo/')

    query = Recepie.objects.all()
    context = {
        'receipes': query
    }
        
    return render(request, 'receipes.html',context)


def delete(request, id):    
    Recepie.objects.get(id=id).delete()
    return redirect('/')


def update(request, id):    
    query = Recepie.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST 
        image = request.FILES.get('image')
        name = data.get('name')
        description = data.get('description')     

        query.name = name
        query.description = description
        query.image = image
        query.save()
        return redirect('/')
    context = {
        'receipes': query
    }
    return render(request, 'update.html' ,context)
 

def login(request):

    if request.method == "POST":
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            return redirect('login/')
        
        user = authenticate(username = username, password = password)        
        if user is None:
            return redirect('/login/')
        else:
            login(request , user)
            return redirect('/')
                
    return render(request, 'login.html') 


def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('user_name')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return redirect('/signup/')
        
        user = User.objects.create_user( first_name=first_name, last_name=last_name ,username=username)
        user.set_password(password)
        user.save()
        return redirect('/signup/')
    
    return render(request, 'register.html')