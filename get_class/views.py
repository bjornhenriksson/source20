from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from get_class.models import GetUrl,Course


def index(request):
    page = request.GET.get('page')
    if not page:
        page = 1
    current_course = request.GET.get('course')
    get_course_id = Course.objects.filter(course_name=current_course)
    get_url_list = GetUrl.objects.filter(current_course=get_course_id, id=page)
    get_previous_id = int(page) - 1
    get_next_id = int(page) + 1
    if GetUrl.objects.filter(id=get_next_id).exists():
        next_page = '<a href="?course=%s&page=%s">next</a>' % (current_course,get_next_id)
    else:
        next_page = 'no more pages'
    if GetUrl.objects.filter(id=get_previous_id).exists():
        prev_page = '<a href="?course=%s&page=%s">prev</a>' % (current_course,get_previous_id)
    else:
        prev_page = 'no previous pages'

    ratio = GetUrl.objects.filter(current_course=get_course_id, id=page)

    context = {
        'get_url_list': get_url_list,
        'prev_page': prev_page,
        'next_page': next_page,
        'current_ratio': ratio,
    }

    return render(request, 'get_class/index.html', context)

def vote_up(request):
     page = request.GET.get('page')
     current_course = request.GET.get('course')
     get_course_id = Course.objects.filter(course_name=current_course)
     find_url = GetUrl.objects.get(current_course=get_course_id, id=page)
     find_url.votes += 1
     find_url.save()
     next_page = int(page) + 1
     return HttpResponseRedirect('/get_class/?course=%s&page=%s' % (current_course, next_page))

def vote_down(request):
     page = request.GET.get('page')
     current_course = request.GET.get('course')
     get_course_id = Course.objects.filter(course_name=current_course)
     find_url = GetUrl.objects.get(current_course=get_course_id, id=page)
     find_url.votes -= 1
     find_url.save()
     next_page = int(page) + 1
     return HttpResponseRedirect('/get_class/?course=%s&page=%s' % (current_course, next_page))





