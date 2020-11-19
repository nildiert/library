from django.shortcuts import render
from .models import Book, Author, Editorial
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import BookSerializer, AuthorSerializer, EditorialSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin


class BookViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class EditorialViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer    