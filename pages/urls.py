# This file is newly created by you and type in all the commands below

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # at url with '', then go to views.py to run the function called 'index', it's named 'index'.
    path('about', views.about, name='about') # similarly, see url 'about' at layer 1, goto views.py to run function called "about"

]