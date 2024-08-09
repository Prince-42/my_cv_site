"""
This module registers the Experience, Education, and Skill models with 
the Django admin site. This makes them accessible for management through the admin interface.
"""
from django.contrib import admin
from .models import Experience, Education, Skill


# Registering the Experience model with the Django admin site
admin.site.register(Experience)

# Registering the Education model with the Django admin site
admin.site.register(Education)

# Registering the Skill model with the Django admin site
admin.site.register(Skill)
