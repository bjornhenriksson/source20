from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from get_class.models import Courses

def index(request):
    page = request.GET.get('page')
    if not page:
        page = 1
    current_course = request.GET.get('course')
    get_url_list = Courses.objects.filter(course_name=current_course, id=page)
    get_previous_id = int(page) - 1
    get_next_id = int(page) + 1
    if Courses.objects.filter(id=get_next_id).exists():
        next_page = '<a href="?course=%s&page=%s">next</a>' % (current_course,get_next_id)
    else:
        next_page = 'no more pages'
    if Courses.objects.filter(id=get_previous_id).exists():
        prev_page = '<a href="?course=%s&page=%s">prev</a>' % (current_course,get_previous_id)
    else:
        prev_page = 'no previous pages'
    context = {
        'get_url_list': get_url_list,
        'prev_page': prev_page,
        'next_page': next_page,
    }
    return render(request, 'get_class/index.html', context)