from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin

from .celery import send_email_task
from .models import Author, Book, Editorial
from .serializers import AuthorSerializer, BookSerializer, EditorialSerializer


class BookViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Class to create, get, update and delete books
    """
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def create(self, request, *args, **kwargs):
        author_id = request.data.get('author').split('/')[-2]
        author = Author.objects.get(id=author_id)
        send_email_task.delay(author.name, author.email, request.data)
        return super(BookViewSet, self).create(request, *args, **kwargs)


class AuthorViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Class to create, get, update and to delete Authors
    """
    permission_classes = (IsAuthenticated,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class EditorialViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Class to create, get, update and to delete Editorials
    """
    permission_classes = (IsAuthenticated,)
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer    

class AuthorBooksViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Class to get all the books by author
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.filter(author=self.kwargs['author_pk'])
    
    