from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def MyView(request):
    return HttpResponse("function base view")
