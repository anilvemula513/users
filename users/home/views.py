from django.utils import timezone
from django.shortcuts import render
from home.models import Cast, Movie
from home.serializers import CastSerializer, MovieSerializer
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



# {
#     "title": "Mayabazar",
#     "runtime": 200,
#     "language": "Telugu",
#     "tagline": "Best Telugu Movie Ever"
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

@api_view(['GET','POST'])
def movies(request):
    if request.method=='GET' :
        objs = Movie.objects.all()
        # print(objs)
        serializer = MovieSerializer(objs,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = MovieSerializer(data = data)
        if serializer.is_valid():
            serializer.created_at = timezone.now()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','POST'])
def movie_details(request,movie_id):
    if request.method=='GET' :
        print(movie_id,'74')
        # try:
        objs = Movie.objects.get(id=movie_id)
        
    
        serializer = MovieSerializer(objs)
        # print(serializer.data,'81')
        cast_objs = list(Cast.objects.filter(movie_id = movie_id).values_list('name'))
        # print(cast_objs)
        # cast_serializer = CastSerializer(cast_objs,many=True)
        # print(cast_serializer.data,'84')
        cast_data = {
            'cast': cast_objs
        }
        output_dict = {**serializer.data,**cast_data}
        return Response(output_dict)
        # except:
        #     data = {
        #         'error' : f"There is no movie with id {movie_id}"
        #     }
        #     return Response(data)
@api_view(['GET','POST'])
def cast(request):
    if request.method=='POST':
        data = request.data
        # print(data,'91')
        serializer = CastSerializer(data=data)

        if serializer.is_valid():
            movie_obj = Movie.objects.get(id=data['movie_id'])
            
            serializer.save(movie_id=data['movie_id'])
            return Response(serializer.data)
        return Response(serializer.errors)    
