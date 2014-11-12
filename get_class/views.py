from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from get_class.models import Courses

def index(request):
    get_url_list = Courses.objects.order_by('-pub_date')[:5]
    template = loader.get_template('get_class/index.html')
    context = RequestContext(request, {
        'get_url_list': get_url_list,
    })
    return HttpResponse(template.render(context))