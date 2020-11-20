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
    
    ```
    python3 -m venv env && source env/bin/activate
    ```
    
* Install libraries and run the django application:

    > You can pass the port you want the app run on in the second argument (In this example the port is the number 8000)

    ```
    ./install_and_run.sh 8000
    ```
    
### Second terminal (Celery Server)

* Enter the following path:

    ```
    cd library/library/
    ```

* Use the environment:

    ```
    source ../env/bin/activate
    ```
    
* Execute celery:

    ```
    celery -A library worker --loglevel=info
    ```



