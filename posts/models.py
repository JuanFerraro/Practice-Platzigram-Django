"""Posts Models."""

# Django
from django.db import models


class User(models.Model):
    """User Model"""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    bio = models.TextField(blank=True, max_length=500)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)