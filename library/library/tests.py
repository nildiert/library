import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from library.library.models import Author, Book, Editorial
from library.library.serializers import AuthorSerializer
from django.urls import reverse


class RegistrationTestcase(APITestCase):
    
    def test_registration(self):
        data = {"username": "testcase", "email": "test@localhost.app",
                "password": "some_strong_psw"}
        response = self.client.post("/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class AuthenticationTokenTestCase(APITestCase):
    
    def setUp(self):
        self.data_first_user = {"username":"nildiert", "password":"some-good-password"}
        self.data_second_user = {"username":"nildiert2", "password":"another-good-password"}
        
        self.user = User.objects.create_user(username="nildiert",
                                             password="some-good-password",
                                             email="test@localhost.com")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        
    def test_token_authentication_success(self):
        response = self.client.post("/api-token-auth/", self.data_first_user)
        response_token = response.data.get('token')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_token, self.token.key)
    
    def test_token_authentication_failure(self):
        response = self.client.post("/api-token-auth/", self.data_second_user)
        response_token = response.data.get('token')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotEqual(response_token, self.token.key)
        
class BookViewSetTestCase(APITestCase):
    
    def setUp(self):
        self.data_first_user = {"username":"nildiert", "password":"some-good-password"}
        self.data_second_user = {"username":"nildiert2", "password":"another-good-password"}
        
        self.author = Author.objects.create(name="Sebastian Raschka",
                                                   birth="13 July 2019 Bangladesh",
                                                   birthdate="2019-06-13",
                                                   nationality="United States",
                                                   occupation="Assistant Professor of Statistics",
                                                   email="sebastianraschka@yopmail.com")
        self.data_first_user = {"username":"nildiert", "password":"some-good-password"}
        self.data_second_user = {"username":"nildiert2", "password":"another-good-password"}
        
        self.editorial = Editorial.objects.create(name="Packt",
                                                            foundation=2003,
                                                            campus="United Kingdom",
                                                            employees=200,
                                                            website="http://www.packtpub.com/")
        self.book_data = { "title": "Python Machine Learning - Third Edition",
                          "publish_date": "2019-12-07",
                          "language": "English",
                          "abstract": """Python Machine Learning, Third Edition is a comprehensive
                          guide to machine learning and deep learning with Python. It acts as both
                          a step-by-step tutorial, and a reference you'll keep coming back to as 
                          you build your machine learning systems.""",
                          "ISBN": "9781789955750",
                          "number_pages": 770,
                          "year": 2019,
                          "author": "http://localhost:8000/authors/1/",
                          "editorial": "http://localhost:8000/editorials/1/"
                          }        
        
        self.user = User.objects.create_user(username="nildiert",
                                             password="some-good-password",
                                             email="test@localhost.com")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        
    def test_book_authenticated(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_book_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_book_create(self):

        response = self.client.post('/books/', data=self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['ISBN'], '9781789955750')
        
    def test_book_detail(self):
        response = self.client.post('/books/', data=self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)                
        
        response = self.client.get('/books/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('title'), "Python Machine Learning - Third Edition")
    
    def test_book_update(self):
        response = self.client.post('/books/', data=self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        updated_data = { "title": "Python Machine Learning",
                          "publish_date": "2019-12-06",
                          "language": "English",
                          "abstract": """Python Machine Learning, Third Edition is a comprehensive
                          guide to machine learning and deep learning with Python.""",
                          "ISBN": "9781789955750",
                          "number_pages": 770,
                          "year": 2019,
                          "author": "http://localhost:8000/authors/1/",
                          "editorial": "http://localhost:8000/editorials/1/"
                          }   
        
        response = self.client.put('/books/1/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('title'), updated_data.get('title'))
        self.assertEqual(response.data.get('publish_date'), updated_data.get('publish_date'))
        self.assertEqual(response.data.get('language'), updated_data.get('language'))
        self.assertEqual(response.data.get('abstract'), updated_data.get('abstract'))
        self.assertEqual(response.data.get('ISBN'), updated_data.get('ISBN'))
        self.assertEqual(response.data.get('number_pages'), updated_data.get('number_pages'))
        self.assertEqual(response.data.get('year'), updated_data.get('year'))
    
    def test_book_delete(self):
        response = self.client.post('/books/', data=self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.delete('/books/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/books/')
        self.assertEqual(Book.objects.count(), len(response.data))


class AuthorViewSetTestCase(APITestCase):
    
    def setUp(self):
        self.data_first_user = {"username": "nildiert", "password":"some-good-password"}
        self.data_second_user = {"username": "nildiert2", "password": "another-good-password"}
        self.user = User.objects.create_user(
            username="nildiert",
            password="some-good-password",
            email="test@localhost.com"
        )
        self.author_data =    {
            "name": "One author name",
            "birth": "13 July 2019 Turquish",
            "birthdate": "2019-06-13",
            "nationality": "Turquish",
            "occupation": "Statistics Research",
            "email": "imranAhmaf@yopmail.com"
        }
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        
    def test_author_authenticated(self):
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_author_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_author_create(self):
        response = self.client.post('/authors/', data=self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "One author name")
        
    def test_author_detail(self):
        response = self.client.post('/authors/', data=self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/authors/', kwargs={'pk': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('name'), "One author name")
        
    def test_author_update(self):
        response = self.client.post('/authors/', data=self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        updated_data =  {
            "name": "Imran Ahmad",
            "birth": "13 July 2019 United states",
            "birthdate": "2019-06-13",
            "nationality": "American",
            "occupation": "Statistics Research",
            "email": "imranAhmad@yopmail.com"
        }
        response = self.client.put('/authors/1/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), updated_data.get("name"))
        self.assertEqual(response.data.get("birth"), updated_data.get("birth"))
        self.assertEqual(response.data.get("birthdate"), updated_data.get("birthdate"))
        self.assertEqual(response.data.get("nationality"), updated_data.get("nationality"))
        self.assertEqual(response.data.get("occupation"), updated_data.get("occupation"))
        self.assertEqual(response.data.get("email"), updated_data.get("email"))
        
        
    def test_author_delete(self):
        response = self.client.post('/authors/', data=self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.delete('/authors/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/authors/')
        self.assertEqual(Author.objects.count(), len(response.data))
        
class EditorialViewSetTestCase(APITestCase):
    
    def setUp(self):
        self.data_first_user = {"username": "nildiert", "password":"some-good-password"}
        self.data_second_user = {"username": "nildiert2", "password": "another-good-password"}
        self.user = User.objects.create_user(
            username="nildiert",
            password="some-good-password",
            email="test@localhost.com"
        )
        self.editorial_data = {
            "name": "Packt",
            "foundation": 2003,
            "campus": "United Kingdom",
            "employees": 200,
            "website": "http://www.packtpub.com/"
        }
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        
    def test_editorial_authenticated(self):
        response = self.client.get('/editorials/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_editorial_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/editorials/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_editorial_create(self):
        response = self.client.post('/editorials/', data=self.editorial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Packt")
        
    def test_editorial_detail(self):
        response = self.client.post('/editorials/', data=self.editorial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/editorials/', kwargs={'pk', 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get('name'), "Packt")
        
    def test_editorial_update(self):
        response = self.client.post('/editorials/', data=self.editorial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        updated_data = {
            "name": "Pearson",
            "foundation": 1980,
            "campus": "United States",
            "employees": 468,
            "website": "http://www.pearson.com/"
        }
        response = self.client.put('/editorials/1/', data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), updated_data.get("name"))
        self.assertEqual(response.data.get("foundation"), updated_data.get("foundation"))
        self.assertEqual(response.data.get("campus"), updated_data.get("campus"))
        self.assertEqual(response.data.get("employees"), updated_data.get("employees"))
        self.assertEqual(response.data.get("website"), updated_data.get("website"))
        
    def test_editorial_delete(self):
        response = self.client.post('/editorials/', data=self.editorial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.delete('/editorials/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/editorials/')
        self.assertEqual(Editorial.objects.count(), len(response.data))
        
class AuthorBooksViewSetTestCase(APITestCase):
    
    def setUp(self):
        self.data_first_user = {"username": "nildiert", "password":"some-good-password"}
        self.data_second_user = {"username": "nildiert2", "password": "another-good-password"}
        self.user = User.objects.create_user(
            username="nildiert",
            password="some-good-password",
            email="test@localhost.com"
        )
        self.editorial_data = {
            "name": "Packt",
            "foundation": 2003,
            "campus": "United Kingdom",
            "employees": 200,
            "website": "http://www.packtpub.com/"
        }
        self.author_data =    {
            "name": "Imran Ahmaf",
            "birth": "13 July 2019 Turquish",
            "birthdate": "2019-06-13",
            "nationality": "Turquish",
            "occupation": "Statistics Research",
            "email": "imranAhmaf@yopmail.com"
        }
        self.first_book_data = { 
            "title": "Python Machine Learning - Third Edition",
            "publish_date": "2019-12-07",
            "language": "English",
            "abstract": """Python Machine Learning, Third Edition is a comprehensive 
                guide to machine learning and deep learning with Python. It acts as both
                a step-by-step tutorial, and a reference you'll keep coming back to as 
                you build your machine learning systems.""",
            "ISBN": "9781789955750",
            "number_pages": 770,
            "year": 2019,
            "author": "http://testserver:8000/authors/1/",
            "editorial": "http://testserver:8000/editorials/1/"
        }             
        self.second_book_data = { 
            "title": "Python Machine Learning - Third Edition",
            "publish_date": "2019-12-07",
            "language": "English",
            "abstract": """Python Machine Learning, Third Edition is a comprehensive 
                guide to machine learning and deep learning with Python. It acts as both
                a step-by-step tutorial, and a reference you'll keep coming back to as 
                you build your machine learning systems.""",
            "ISBN": "9781789955750",
            "number_pages": 770,
            "year": 2019,
            "author": "http://testserver:8000/authors/1/",
            "editorial": "http://testserver:8000/editorials/1/"
        }             
        
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        
    def test_author_books_authenticated(self):
        response = self.client.get('/authors/1/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_author_books_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/authors/1/books/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_author_books_list(self):
        response = self.client.get('/authors/1/books/')
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post('/authors/', data=self.author_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('/editorials/', data=self.editorial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('/books/', data=self.first_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/authors/1/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Book.objects.all().count())
        response = self.client.post('/books/', data=self.second_book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/authors/1/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Book.objects.all().count())
        response = self.client.get('/authors/2/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        