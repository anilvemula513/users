from dataclasses import fields
from rest_framework import serializers
from .models import Cast, Movie
from django.contrib.auth.models import User




class CastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cast
        fields = '__all__'
        
    
class MovieSerializer(serializers.ModelSerializer):
    cast = CastSerializer(read_only=True,many=True)
    class Meta:
        model = Movie
        fields = '__all__'

    def validate(self,data):

        if data['tagline']=="hi":
            raise serializers.ValidationError("tagline shouldn't be hi")
        


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user