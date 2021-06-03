from django.contrib import admin
from django.urls import path

#important user addition
from . import views 
from django.conf.urls import include 
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path(r'', views.cake, name='cake' ),
    path(r'favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('homeimgs/favicon.png'))),
]