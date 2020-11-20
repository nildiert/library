# Library API

## Installation

1. Open two terminals

### First terminal (Django server)


* Clone the repo
    ```bash
    git clone https://github.com/nildiert/library.git &&  cd library
    ```
* Create an environment:
    
    If you don't have python3-env, you can install it as follows
    ```bash
    sudo apt-get update -y
    sudo apt-get install python3-venv -y
    ```
    
    If you have installed venv, then run this command:
    
    ```bash
    python3 -m venv env && source env/bin/activate
    ```
    
* Install libraries and run the django application:

    > You can pass the port you want the app run on in the second argument (In this example the port is the number 8000)

    ```bash
    ./install_and_run.sh 8000
    ```
    
### Second terminal (Celery Server)

* Enter the following path:

    ```bash
    cd library/library/
    ```

* Use the environment:

    ```bash
    source ../env/bin/activate
    ```
    
* Execute celery:

    ```bash
    celery -A library worker --loglevel=info
    ```



## Tests

After finishing the installation, you can run the tests as follows:

    ```bash
    python manage.py test
    ```




## REST API

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

> Local

```bash
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"nildiert", "password": "pass123", "email": "nildiert@gmail.com"}' http://localhost:8000/users/

```
> Deployed app

```bash
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"nildiert", "password": "pass123", "email": "nildiert@gmail.com"}' http://18.228.221.128:8000/users/

```


### Response

```
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

```bash
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

```bash
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
