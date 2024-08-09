"""
This module contains the configuration class for the 'cv' Django application.

The CvConfig class is used to configure settings specific to the 'cv' application.
It defines the default type of auto-generated primary key field for models 
and the name of the application.
"""
from django.apps import AppConfig


class CvConfig(AppConfig):
    """Configuration class for the 'cv' Django application.

    Args:
        default_auto_field (str): The type of auto-generated primary key field to use for models.
        name (str): The name of the application, which is 'cv' in this case.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cv'
