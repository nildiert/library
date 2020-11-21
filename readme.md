# Library API

This API Rest is responsible for saving information for a library of books, there you can save and consult information about books, authors and publishers.


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
cd library/
```

```
$ pwd
>> ~/projects/library/library
```

* Use the environment:

```bash
source ../env/bin/activate
```
    
* Execute celery:

```bash
celery -A api worker --loglevel=info
```



## Tests

After finishing the installation, you can run the tests as follows:

```bash
python manage.py test
```

## Examples

Yo can see the examples of the api [here](https://github.com/nildiert/library/tree/main/examples).



## Author

Nildiert Jimenez Jaramillo

## Changelog

20 Nov - 2020. Creation

