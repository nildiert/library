from django.contrib import admin

from .models import Author, Book, Editorial

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Editorial)

# Register your models here.
