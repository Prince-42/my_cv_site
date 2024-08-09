"""
Defines URL patterns for the CV application.

This module maps URLs to corresponding views in the 'views.py' file. The main URL pattern is:

- '': The root URL, mapped to the 'cv_home' view function.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_home, name='cv_home'),
    path('cv/', views.cv_page, name='cv_page'),
    path('contact/', views.contact, name='contact'),
    
]
