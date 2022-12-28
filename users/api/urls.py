from home.views import RegisterAPI, cast, index, movie_details, movies
from django.urls import path
from knox import views as knox_views
from home.views import LoginAPI

urlpatterns = [
    path('index/', index),
    path('movie/',movies),
    path('movie/<int:movie_id>/',movie_details),
    path('cast/',cast),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

    
