

# REST API

The REST API to the example app is described below.


### USERS

#### Create a new User


### Request

`POST /users/`

```json
{
    "username": "nildiert",
    "password": "pass123",
    "first_name"" "nildiert",
    "last_name": "jimenez"
    "email": "nildiert@gmail.com"
}
```


```bash
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"nildiert", "password": "pass123", "email": "nildiert@gmail.com"}' http://localhost:8000/users/

```


### Response

```json
HTTP/1.1 201 Created
Date: Fri, 20 Nov 2020 19:55:40 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 87
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":4,"username":"user","first_name":"","last_name":"","email":"email@localhost.com"}
```


### TOKEN

#### Get the Auth token


### Request

`POST /users/`

```json
{
    "username": "nildiert",
    "password": "pass123",
}
```

> Local

```bash
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"user", "password": "pass" }' http://localhost:8000/api-token-auth/

```



### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 20:10:19 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Allow: POST, OPTIONS
X-Frame-Options: DENY
Content-Length: 147
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"token":"62b07a742c77929eda3fda02646ff9dfc564da51","user":{"id":4,"username":"user","first_name":"","last_name":"","email":"email@localhost.com"}} 

```


### AUTHORS

### Create a new Author


#### Request

`POST /authors/`

```json
    {
    "name": "Antonio Mele",
    "birth": "13 July 2019 Colombia",
    "birthdate": "2019-06-13",
    "nationality": "Colombian",
    "occupation": "certified Google Instructor",
    "email": "antoniomele@yopmail.com"

}
```


```bash
curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  -d '{ "name": "Antonio Mele", "birth": "13 July 2019 Colombia", "birthdate": "2019-06-13", "nationality": "Colombian","occupation": "certified Google Instructor", "email": "antoniomele@yopmail.com" }' http://localhost:8000/authors/

```


#### Response

```json
HTTP/1.1 201 Created
Date: Fri, 20 Nov 2020 20:57:26 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 190
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":7,"name":"Antonio Mele","birth":"13 July 2019 Colombia","birthdate":"2019-06-13","nationality":"Colombian","occupation":"certified Google Instructor","email":"antoniomele@yopmail.com"}

```



### Get a specific Author


#### Request

`GET /authors/id/`




```bash
curl -i -H 'Accept: application/json' -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51" http://localhost:8000/authors/1/

```


#### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 20:39:11 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 190
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":5,"name":"Antonio Mele","birth":"13 July 2019 Colombia","birthdate":"2019-06-13","nationality":"Colombian","occupation":"certified Google Instructor","email":"antoniomele@yopmail.com"}

```


### Get all the Authors


#### Request

`GET /authors/`



```bash
curl -i -H 'Accept: application/json' -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51" http://localhost:8000/authors/


```


#### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 20:41:12 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 953
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin


[{"id":1,"name":"Antonio Mele","birth":"13 July 2019 Colombia","birthdate":"2019-06-13","nationality":"Colombian","occupation":"certified Google Instructor","email":"antoniomele@yopmail.com"}]

```

### Update Author


#### Request

`PUT /authors/id/`




```bash
curl -i -X PUT -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  -d '{ "name": "Antonio Mele", "birth": "13 July 2019 United States", "birthdate": "2019-06-13", "nationality": "American","occupation": "certified Google Instructor", "email": "antoniomele@yopmail.com" }' http://localhost:8000/authors/1/

```


#### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 20:49:17 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 194
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":1,"name":"Antonio Mele","birth":"13 July 2019 United States","birthdate":"2019-06-13","nationality":"American","occupation":"certified Google Instructor","email":"antoniomele@yopmail.com"}

```


### Delete Author


#### Request

`DELETE /authors/id/`



```bash
curl -i -X DELETE -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  http://localhost:8000/authors/1/

```


#### Response

```json
HTTP/1.1 204 No Content
Date: Fri, 20 Nov 2020 20:52:08 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 0
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

```

---



### EDITORIALS

### Create a new editorial


#### Request

`POST /editorials/`

```json
{
    "name": "Packt",
    "foundation": 2003,
    "campus": "United Kingdom",
    "employees": 200,
    "website": "http://www.packtpub.com/"

}
```


```bash
curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  -d '   {"name": "Packt", "foundation": 2003, "campus": "United Kingdom", "employees": 200, "website": "http://www.packtpub.com/"}' http://localhost:8000/editorials/

```


#### Response

```json
HTTP/1.1 201 Created
Date: Fri, 20 Nov 2020 21:05:59 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 120
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":3,"name":"Packt","foundation":2003,"campus":"United Kingdom","employees":200,"website":"http://www.packtpub.com/"}

```

---


### Get a specific Editorial


#### Request

`GET /editorials/id/`




```bash
curl -i -H 'Accept: application/json' -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51" http://localhost:8000/editorials/3/

```


#### Response

```json
localhost:8000/editorials/3/
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 21:07:38 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 120
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":3,"name":"Packt","foundation":2003,"campus":"United Kingdom","employees":200,"website":"http://www.packtpub.com/"}

```


### Get all the editorials


#### Request

`GET /editorials/`



```bash
curl -i -H 'Accept: application/json' -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51" http://localhost:8000/editorials/


```


#### Response

```json
localhost:8000/editorials/
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 21:08:27 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 365
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

[{"id":3,"name":"Packt","foundation":2003,"campus":"United Kingdom","employees":200,"website":"http://www.packtpub.com/"}]

```

### Update Editorial


#### Request

`PUT /editorials/id/`


```bash
curl -i -X PUT -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  -d '{"name":"Oreilly","foundation":1999,"campus":"United States","employees":400,"website":"http://www.oreilly.com/"}' http://localhost:8000/editorials/3/

```


#### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 21:11:07 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 194
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":1,"name":"Antonio Mele","birth":"13 July 2019 United States","birthdate":"2019-06-13","nationality":"American","occupation":"certified Google Instructor","email":"antoniomele@yopmail.com"}

```


### Delete Editorial


#### Request

`DELETE /editorials/id/`


```bash
curl -i -X DELETE -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  http://localhost:8000/editorials/1/

```


#### Response

```json
HTTP/1.1 204 No Content
Date: Fri, 20 Nov 2020 21:13:27 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 0
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

```


---



### BOOKS

### Create a new book


#### Request

`POST /books/`

```json
{
    "title": "30 Algorithms Every Programmer Should Know",
    "publish_date": "2020-06-18",
    "language": "English",
    "abstract": "Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.",
    "ISBN": "9781789801217",
    "number_pages": 382,
    "year": 2020,
    "author": "http://localhost:8000/authors/1/",
    "editorial": "http://localhost:8000/editorials/3/"
}
```


```json
curl -i -X POST -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  -d '  { "title": "30 Algorithms Every Programmer Should Know", "publish_date": "2020-06-18", "language": "English", "abstract": "Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.", "ISBN": "9781789801217", "number_pages": 382, "year": 2020, "author": "http://localhost:8000/authors/1/", "editorial": "http://localhost:8000/editorials/3/" }' http://localhost:8000/books/

```


#### Response

```json
HTTP/1.1 201 Created
Date: Fri, 20 Nov 2020 21:23:16 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 674
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":19,"title":"30 Algorithms Every Programmer Should Know","publish_date":"2020-06-18","language":"English","abstract":"Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.","ISBN":"9781789801217","number_pages":382,"year":2020,"author":"http://localhost:8000/authors/1/","editorial":"http://localhost:8000/editorials/3/"}

```



### Get a specific Book


#### Request

`GET /books/id/`




```json
curl -i -H 'Accept: application/json' -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51" http://localhost:8000/books/19/

```


#### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 21:24:57 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 674
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":19,"title":"30 Algorithms Every Programmer Should Know","publish_date":"2020-06-18","language":"English","abstract":"Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.","ISBN":"9781789801217","number_pages":382,"year":2020,"author":"http://localhost:8000/authors/1/","editorial":"http://localhost:8000/editorials/3/"}

```


### Get all the books


#### Request

`GET /books/`



```json
curl -i -H 'Accept: application/json' -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51" http://localhost:8000/books/


```


#### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 21:25:53 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 1351
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

[{"id":19,"title":"30 Algorithms Every Programmer Should Know","publish_date":"2020-06-18","language":"English","abstract":"Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.","ISBN":"9781789801217","number_pages":382,"year":2020,"author":"http://localhost:8000/authors/1/","editorial":"http://localhost:8000/editorials/3/"}]

```

### Update Book


#### Request

`PUT /books/id/`


```json
curl -i -X PUT -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  -d '{"title":"30 Algorithms Every Programmer Should Know","publish_date":"2020-06-18","language":"English","abstract":"Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.","ISBN":"9781781581217","number_pages":200,"year":1992,"author":"http://localhost:8000/authors/1/","editorial":"http://localhost:8000/editorials/3/"}' http://localhost:8000/books/19/

```


#### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 21:28:29 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 674
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

{"id":19,"title":"30 Algorithms Every Programmer Should Know","publish_date":"2020-06-18","language":"English","abstract":"Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.","ISBN":"9781781581217","number_pages":200,"year":1992,"author":"http://localhost:8000/authors/1/","editorial":"http://localhost:8000/editorials/3/"}

```


### Delete book


#### Request

`DELETE /editorials/id/`



```json
curl -i -X DELETE -H "Content-Type: application/json" -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51"  http://localhost:8000/books/18/

```


#### Response

```json
HTTP/1.1 204 No Content
Date: Fri, 20 Nov 2020 21:31:17 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Vary: Accept
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 0
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

```


---






### BOOKS BY AUTHOR



### Get all the books by author


#### Request

`GET /authors/id/books/`



```json
curl -i -H 'Accept: application/json' -H "Authorization: Token 62b07a742c77929eda3fda02646ff9dfc564da51" http://localhost:8000/authors/1/books/


```


#### Response

```json
HTTP/1.1 200 OK
Date: Fri, 20 Nov 2020 21:34:25 GMT
Server: WSGIServer/0.2 CPython/3.8.6
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
Content-Length: 676
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin

[{"id":19,"title":"30 Algorithms Every Programmer Should Know","publish_date":"2020-06-18","language":"English","abstract":"Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.","ISBN":"9781781581217","number_pages":200,"year":1992,"author":"http://localhost:8000/authors/1/","editorial":"http://localhost:8000/editorials/3/"}]

```





## Author

Nildiert Jimenez Jaramillo

## Changelog

20 Nov - 2020. Creation

