from django.shortcuts import render  #important user addition
from django.http import HttpResponse  #important user addition

#important user addition
from .models import *
from django.template import loader
from django.http import Http404
# Create your views here.



def capsules(request):
    template=loader.get_template('capsules/capsules.html')
    infos={
        
    }

    return HttpResponse(template.render(infos,request))
