from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from user.models import Progress
from django.contrib.auth.models import User

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

def exists(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        if User.objects.filter(username=new_username).exists():
            return render(request, 'user/register.html', {"msg": "This username already exists"})


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/')
    if request.method == 'POST':
        email = request.POST['email']
        new_username = request.POST['username']
        validate_email = "grey"
        validate_user = "grey"
        ready_email = False
        ready_user = False

        if User.objects.filter(username=new_username).exists():
            msg_user = "this username already exists"
            validate_user = "pink"
        elif len(new_username) > 4:
            msg_user = "perfect!"
            validate_user = "green"
            ready_user = True
        elif len(new_username) <= 4:
            msg_user = "needs to be longer than 4 characters"
            validate_user = "pink"

        if User.objects.filter(email=email).exists():
            msg_email = "this email already exists"
            validate_email = "pink"
        elif len(email) > 4:
            msg_email = "perfect!"
            validate_email = "green"
            ready_email = True
        elif len(email) <= 4:
            msg_email = "needs to be longer than 4 characters"
            validate_email = "pink"

        if ready_email or ready_user:
            msg = "Almost there!"
        else:
            msg = "Mother-Fudgin' Fiddle-Sticks!"


        context = {
            'msg_user': msg_user,
            'msg_email': msg_email,
            'save_user': new_username,
            'save_email': email,
            'validate_user': validate_user,
            'validate_email': validate_email,
            'msg': msg,
        }
        return render(request, 'user/register.html', context)
    else:
        return render(request, 'user/register.html', {"msg": "Register below"})


def tracker(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/user/')
    user = request.user
    p = Progress.objects.filter(user=user)[:1]
    return render(request, 'user/landing.html', {"stats": p})
