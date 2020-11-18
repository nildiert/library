from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    birth = models.CharField(max_length=100)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)
    occupation = models.CharField(max_length=50)

class Editorial(models.Model):
    name = models.CharField(max_length=50)
    foundation = models.IntegerField()
    campus = models.CharField(max_length=50)
    employees = models.IntegerField()
    website = models.URLField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    language = models.CharField(max_length=20)
    abstract = models.CharField(max_length=500)
    ISBN = models.CharField(max_length=20)
    number_pages = models.IntegerField()
    year = models.IntegerField()
    

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
