"""
This module registers the Experience, Education, and Skill models with 
the Django admin site. This makes them accessible for management through the admin interface.
"""
from django.contrib import admin
from .models import Experience, Education, Skill


# Register your models here.
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
