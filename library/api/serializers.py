from rest_framework import serializers

from .models import Author, Book, Editorial


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Author Serializer
    """
    class Meta:
        model = Author
        fields = ['id','name', 'birth', 'birthdate', 'nationality', 'occupation', 'email']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    """
    Book Serializer
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publish_date', 'language', 'abstract',
                  'ISBN', 'number_pages', 'year', 'author', 'editorial']
        
    
class EditorialSerializer(serializers.HyperlinkedModelSerializer):
    """
    Editorial Serializer
    """
    books = serializers.HyperlinkedRelatedField(many=False,
                                                view_name='books-detail',
                                                read_only=True)
    class Meta:
        model = Editorial
        fields = ['id','name', 'foundation', 'campus', 'employees', 'website', 'books']
        
         