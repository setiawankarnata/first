from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from rest_framework import viewsets
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
