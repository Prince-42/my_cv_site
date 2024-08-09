"""
This module defines models for storing resume data, including experience, education, and skills.
"""
from django.db import models

# Create your models here.


class Experience(models.Model):
    """Represents a professional experience in a resume.

    Attributes:
        company (str): The name of the company where the experience took place.
        title (str): The job title held during the experience.
        start_date (date): The start date of the experience.
        end_date (date, optional): The end date of the experience (null for current positions).
        description (str): A description of the responsibilities and accomplishments.
    """
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True,
                                blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    """Represents an educational entry in a resume.

    Attributes:
        school (str): The name of the educational institution.
        degree (str): The degree or certification obtained.
        start_date (date): The start date of the education.
        end_date (date, optional): The end date of the education (null for ongoing studies).
    """

    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} from {self.school}"


class Skill(models.Model):
    """Represents a skill listed in a resume.

    Attributes:
        name (str): The name of the skill.
        proficiency (str, optional): The proficiency level (e.g., "Beginner," 
        "Intermediate," "Expert").
    """
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
