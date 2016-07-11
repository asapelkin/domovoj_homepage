from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context, Template

def server_info(request):
    template = loader.get_template('server_info.html')
    return HttpResponse(template.render())

# Create your views here.
