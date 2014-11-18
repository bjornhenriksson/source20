from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from login.models import Progress

def trylogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('landing/')
            else:
                return render(request, 'login/index.html', {"error_msg": "This account seems to be disabled"})
        else:
            return render(request, 'login/index.html', {"error_msg": "Invalid login, try again"})
    else:
        return render(request, 'login/index.html', {"error_msg": "Login below"})

def tracker(request):
    user = request.user
    p = Progress.objects.filter(user=user)
    return render(request, 'login/landing.html', {"stats": p})
