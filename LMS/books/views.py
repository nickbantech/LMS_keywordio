import re
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from books.models import Books
from books.serializers import BookSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BookList(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
   
    def get(self,request,format=None):
        book = Books.objects.all()
        serializer = BookSerializer(book,many = True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = BookSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class BookDetail(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
   
    def get_object(self,pk):
        try:
            return Books.objects.get(pk=pk)   
        except Books.DoesNotExist:
            raise Http404     

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
                  
    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class Student(APIView):
    def get(self,request,format=None):
        book = Books.objects.all()
        serializer = BookSerializer(book,many = True)
        return Response(serializer.data)



