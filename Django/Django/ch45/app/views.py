from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# function base view
def myview(request):
    return HttpResponse("function base view")


# class base veiw
class Myview(View):
    def get(self,request):
        return HttpResponse('class base view' )