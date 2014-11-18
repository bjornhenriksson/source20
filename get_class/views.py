from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from get_class.models import GetUrl,Course
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')

    current_course = request.GET.get('course')
    get_course_id = Course.objects.filter(course_name=current_course)
    get_url_list = GetUrl.objects.filter(current_course=get_course_id).order_by('-votes')
    paginator = Paginator(get_url_list, 1)
    page = request.GET.get('page')

    try:
        urls = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        urls = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        urls = paginator.page(paginator.num_pages)

    return render(request, 'get_class/index.html', {"urls": urls, "course": current_course, 'current_user': request.user})

def vote_up(request):
     id = request.GET.get('id')
     page = request.GET.get('page')
     current_course = request.GET.get('course')
     get_course_id = Course.objects.filter(course_name=current_course)
     find_url = GetUrl.objects.get(current_course=get_course_id, id=id)
     find_url.votes += 1
     find_url.save()
     next_page = int(page) + 1
     return HttpResponseRedirect('/get_class/?course=%s&page=%s' % (current_course, next_page))

def vote_down(request):
     id = request.GET.get('id')
     page = request.GET.get('page')
     current_course = request.GET.get('course')
     get_course_id = Course.objects.filter(course_name=current_course)
     find_url = GetUrl.objects.get(current_course=get_course_id, id=id)
     find_url.votes -= 1
     find_url.save()
     next_page = int(page) + 1
     return HttpResponseRedirect('/get_class/?course=%s&page=%s' % (current_course, next_page))

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')






