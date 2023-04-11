from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from . serializers import BookSerializer

# Create your views here.

class BookAPIView(generics.ListAPIView):
    """A read-only endpoint on all book instances"""
    queryset=Book.objects.all()
    serializer_class=BookSerializer

