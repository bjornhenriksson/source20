from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from user.models import Progress

def redirect(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/landing/')
    else:
        return HttpResponseRedirect('/user/login/')

def trylogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/landing/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/user/landing/')
            else:
                return render(request, 'user/index.html', {"error_msg": "This account seems to be disabled"})
        else:
            return render(request, 'user/index.html', {"error_msg": "Invalid user, try again"})
    else:
        return render(request, 'user/index.html', {"error_msg": "Log in"})

def register(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user/')
    

def tracker(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user/')
    user = request.user
    p = Progress.objects.filter(user=user)[:1]
    return render(request, 'user/landing.html', {"stats": p})
