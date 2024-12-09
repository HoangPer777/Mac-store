from django.shortcuts import render
from django.http import HttpResponse #test
from django.template import loader

def get_home(request):
    template = loader.get_template('userHome.html') #link html
    return HttpResponse(template.render())

