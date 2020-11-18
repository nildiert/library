from rest_framework import serializers
from .models import Book, Author, Editorial



class BookSerializer(serializers.HyperlinkedModelSerializer):
    
    author = serializers.HyperlinkedRelatedField(many=False, view_name='author-detail', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'publish_date', 'language', 'abstract',
                  'ISBN', 'number_pages', 'year', 'author', 'editorial']
        
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Author
        
        fields = ['id','name', 'birth', 'birthdate', 'nationality', 'occupation']
    
    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super(AuthorSerializer, self).get_serializer(*args, **kwargs)
    
class EditorialSerializer(serializers.HyperlinkedModelSerializer):
    
    books = serializers.HyperlinkedRelatedField(many=False, view_name='books-detail', read_only=True)
    
    class Meta:
        model = Editorial
        fields = ['name', 'foundation', 'campus', 'employees', 'website', 'books']
        
         