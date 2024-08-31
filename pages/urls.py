# This file is newly created by you and type in all the commands below

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #go to views.py to run the function called index there, it's named 'index'.
]