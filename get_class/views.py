from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from get_class.models import Courses

def index(request):
    page = request.GET.get('page')
    current_course = request.GET.get('course')
    get_url_list = Courses.objects.filter(course_name=current_course, id=page)
    template = loader.get_template('get_class/index.html')
    context = RequestContext(request, {
        'get_url_list': get_url_list,
    })
    return HttpResponse(template.render(context))