from django.shortcuts import render  #important user addition
from django.http import HttpResponse  #important user addition



#important user addition
from .models import *
from django.template import loader
from django.http import Http404

def cake(request):
# connecting to database

                           
    template=loader.get_template('home.html')
    infos={
        'customers':'customers',
    }

    return HttpResponse(template.render(infos,request))