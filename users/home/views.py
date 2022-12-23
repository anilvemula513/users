from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.


# Following are the models that have to be included:
# 1. Movie
# 2. Cast
# Movie Object:
# {
# id: integer
# title: string
# created_at: datetime(iso 8601)
# updated_at: datetime(iso 8601)
# runtime:integer
# language: string
# tagline: string
# }

# Cast Object:
# {
# id:integer
# name: string
# gender:string
# dob: date
# }

@api_view(['GET'])
def index(request):
    movies = {
        'title' : 'Mayabajar',
        'runtime' : 200,
        'language' : 'telugu',
        'tagline' : 'Best Telugu Movie Ever'
    }
    return Response(movies)