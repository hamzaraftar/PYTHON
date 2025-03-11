from django.shortcuts import render


def home(request):
    ct = request.session.get('counter', 0)
    new = ct + 1
    request.session['counter'] = new
    return render(request, 'home.html' , {'counter': new})