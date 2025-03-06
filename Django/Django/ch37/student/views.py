from django.shortcuts import render


def set_session(request):
    request.session['name'] = 'hamza'
    return render(request , 'student/setsession.html')

def get_session(request):
    name = request.session['name'] 
    return render(request , 'student/getsession.html' , {'name':name})