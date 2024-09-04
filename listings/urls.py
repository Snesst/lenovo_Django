# This file is newly created by you and type in all the commands below

from django.urls import path
from . import views

urlpatterns = [
    path('listings', views.listings, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'), 
]