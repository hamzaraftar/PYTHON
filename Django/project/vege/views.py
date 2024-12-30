from django.shortcuts import render,redirect
from .models import Recepie

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
    return render(request, 'login.html') 

def register(request):
    return render(request, 'register.html')