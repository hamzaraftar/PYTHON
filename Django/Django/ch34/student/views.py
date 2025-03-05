from django.shortcuts import render

# Create your views here.
def show_detail(req):
    return render(req , 'student/show.html')