from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ebook
        fields = ['id','title', 'review', 'favorite', 'author', 'genre']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =['username' , 'password']
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username']) 
        user.set_password(validated_data['password'])
        user.save()
        return user  