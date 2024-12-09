from django.shortcuts import render
from django.http import HttpResponse #test
from django.template import loader

def home(request):
    # return HttpResponse("Hello world!") #test 
    template = loader.get_template('home.html') #link html
    return HttpResponse(template.render())

