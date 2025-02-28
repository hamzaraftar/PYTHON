from django.shortcuts import render
from .models import Profile
# Create your views here.
def all_data(req):
    stu = Profile.objects.all()