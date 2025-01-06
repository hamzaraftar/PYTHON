from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

def index(request):
    feature = Feature.objects.all()
    return render(request, 'index.html',{'features' :feature } )

def counter(request):
    return render(request, 'counter.html')
