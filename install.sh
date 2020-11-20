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
pip install -r requirements.txt

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