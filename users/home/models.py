from turtle import title
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    runtime = models.IntegerField()
    language = models.CharField(max_length=50)
    tagline = models.CharField(max_length=250)