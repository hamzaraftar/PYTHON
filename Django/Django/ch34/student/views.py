from django.shortcuts import render

# Create your views here.
def show_detail(req ,id):
    return render(req , 'student/show.html',{"id":id})