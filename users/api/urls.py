from home.views import cast, index, movie_details, movies
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('movie/',movies),
    path('movie/<int:movie_id>/',movie_details),
    path('cast/',cast)

    
]
