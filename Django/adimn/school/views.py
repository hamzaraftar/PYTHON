from django.shortcuts import render
from school.models import Profile

# Create your views here.
def home(request):
    stu = Profile.objects.all()
    return render(request, 'index.html')