# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
from rest_framework.response import Response

from .models import Book
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .serializers import BookSerializer, BookMiniSerializer
from rest_framework.permissions import IsAuthenticated


class BookViewSet(viewsets.ModelViewSet):
    # serializer_class = BookSerializer
    serializer_class = BookMiniSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)
