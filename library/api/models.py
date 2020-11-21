from django.db import models

class Author(models.Model):
    """
    Author Model
    """
    name = models.CharField(max_length=50)
    birth = models.CharField(max_length=100)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)
    occupation = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Editorial(models.Model):
    """
    Editorial Model
    """
    name = models.CharField(max_length=50)
    foundation = models.IntegerField()
    campus = models.CharField(max_length=50)
    employees = models.IntegerField()
    website = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book Model
    """
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    language = models.CharField(max_length=20)
    abstract = models.CharField(max_length=500)
    ISBN = models.CharField(max_length=20)
    number_pages = models.IntegerField()
    year = models.IntegerField()
    

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
