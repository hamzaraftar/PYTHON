from django.shortcuts import render

def set_session(request):
    request.session['name'] = 'hamza'
    request.session['lname'] = 'asghar'
    return render(request , 'student/setsession.html')

def get_session(request):
    # name = request.session['name'] 
    name = request.session.get('name')
    lname = request.session.get('lname')
    return render(request , 'student/getsession.html' , {'name':name , 'lname':lname})

def del_session(request):
    request.session.flush()
    return render(request , 'student/deletesession.html')
