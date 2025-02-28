from django.shortcuts import render

# Exaple 1 Variable
# def home(req):
#     return render(req , 'app/home.html',context={'name':'hamza asghar'})

# Exaple 2 Filter
def home(req):
    return render(req , 'app/home.html',context={'name':'hamza asghar'})