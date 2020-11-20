#!/usr/bin/bash

python3 -m venv env
source env/bin/activate


echo 
echo "************************************************"
echo "*                                              *"
echo "*           Installing requirements ...        *"
echo "*                                              *"
echo "************************************************"
echo ""
echo ""

python -m pip install --upgrade pip
pip install django
pip install djangorestframework
pip install httpie
# pip install drf-extensions
pip install -U git+git://github.com/chibisov/drf-extensions.git@8001a440c7322be26bbe2d16f3a334a8b0b5860b
pip install pep8
pip install drf-nested-routers
pip install redis
pip install celery


echo 
echo "************************************************"
echo "*                                              *"
echo "*            Making migrations ...             *"
echo "*                                              *"
echo "************************************************"
echo ""
echo ""
python3 manage.py makemigrations

echo 
echo "************************************************"
echo "*                                              *"
echo "*            Migrating db ...                  *"
echo "*                                              *"
echo "************************************************"
echo ""
python3 manage.py migrate

echo 
echo "************************************************"
echo "*                                              *"
echo "*            Running tests ...                 *"
echo "*                                              *"
echo "************************************************"
echo ""

python3 manage.py test

echo 
echo "************************************************"
echo "*                                              *"
echo "*         All tests was successfully           *"
echo "*                 executed!                    *"
echo "*                                              *"
echo "************************************************"
echo 

echo 
echo "************************************************"
echo "*                                              *"
echo "*                Running Server ...            *"
echo "*                                              *"
echo "************************************************"
echo 

python3 manage.py runserver