from operator import mod
from pyexpat import model
from django.db import models


class Candidate(models.Model):
    username = models.CharField(max_length=200)
    bio = models.CharField(max_length=200, blank=True, null=True)
    avatar_url = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    html_url = models.CharField(max_length=200, blank=True, null=True)
