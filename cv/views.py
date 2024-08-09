"""
Defines views for the CV application.

This module contains the view functions responsible for rendering
CV-related templates, primarily the home page.
The main view function is:

- cv_home(request): Retrieves experience, education, and skill data from the database,
                    and renders the 'cv/cv_home.html' template with this context.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Experience, Education, Skill

# Create your views here.


def logged_out(request):
    """Renders the logged out template after user logout"""
    return render(request, 'registration/logged_out.html')

def register(request):
    """Handles user registration.
    If the request method is POST, it process the registration form. If the form 
    is valid, it saves the new user and redirects to the login page with a sucess
    message. If the form has errors, it displays them. for GET request, it renders
    the registration form. 
    
    Args:
        request: The HTTP request object. 
    
    Returns:
        HttpResponse: The rendered registratin page with the form
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')

        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

@login_required
def cv_home(request):
    """Renders the home page of the CV application.
    """
    return render(request, 'cv/cv_home.html')

@login_required
def cv_page(request):
    """Renders the CV page with experience, education, and skills.

    Retrieves all experience, education, and skill entries from the database and passes them
    to the 'cv/cv_page.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered CV page template with the context.
    """
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    context = {
        'experiences': experiences,
        'education': education,
        'skills': skills
    }
    return render(request, 'cv/cv_page.html', context)

@login_required
def contact(request):
    """Renders the contact page.

    This view is accessible only to logged-in users and renders the 'cv/contact.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered contact page template.
    """
    return render(request, 'cv/contact.html')
