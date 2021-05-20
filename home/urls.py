from django.contrib import admin
from django.urls import path

#important user addition
from . import views 
from django.conf.urls import include 
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path(r'capsules',include('capsules.urls') ),
    path(r'', views.home, name='home' ),
    path(r'topic', views.topic, name='topic' ),
    path(r'login', views.login, name='login' ),
    path(r'capsule', views.capsule, name='capsule' ),
    path(r'capdata', views.capdata, name='capdata' ),
    path(r'deletecapsule', views.deletecapsule, name='deletecapsule' ),
    path(r'editcapsule', views.editcapsule, name='editcapsule' ),
    path(r'editusercapsule', views.editusercapsule, name='editusercapsule' ),
    path(r'capsulein', views.capsulein, name='capsulein' ),
    path(r'signup', views.signup, name='signup' ),
    path(r'checkemail', views.checkemail, name='checkemail' ),
    path(r'checkuser', views.checkuser, name='checkuser' ),
    path(r'addnewcapsule', views.addnewcapsule, name='addnewcapsule' ),
    path(r'addusercapsule', views.addusercapsule, name='addusercapsule' ),
    path(r'favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('homeimgs/favicon.png'))),


]
