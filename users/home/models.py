from turtle import title
from unicodedata import name
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    runtime = models.IntegerField()
    language = models.CharField(max_length=50)
    tagline = models.CharField(max_length=250)

class Cast(models.Model):
    GENDER_CHOICES = (('Male','Male'),('Female','Female'),('Transgender','Transgender'),('Rather Not to Say','Rather Not to Say'))
    movie = models.ForeignKey(Movie,to_field='id',null=True,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=150)
    gender = models.CharField(max_length=150,choices=GENDER_CHOICES)
    dob = models.DateField()