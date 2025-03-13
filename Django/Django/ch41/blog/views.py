from django.shortcuts import render
from .models import Blog


def home(request):
    blog = Blog.objects.all()
    return render(request , 'index.html'  ,{'blog':blog})