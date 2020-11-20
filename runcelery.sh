#!/usr/bin/bash

cd library

echo 
echo "************************************************"
echo "*                                              *"
echo "*            Running Celery ...                *"
echo "*                                              *"
echo "************************************************"
echo ""

celery -A library worker -l info