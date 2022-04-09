from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import  serializers
from .models import Books

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']



class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['id','title','author','publication']