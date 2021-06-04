from django.contrib import admin
from django.urls import path

#important user addition
from . import views 
from django.conf.urls import include 



urlpatterns = [
    
    path(r'', views.capsules, name='capsules' ),


]
