from dataclasses import fields
from rest_framework import serializers
from .models import Cast, Movie



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
        