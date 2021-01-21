#!/bin/sh
#python manage.py makemigrations
#python manage.py migrate
mv dump/data/ /mopga/static/
mv dump/data .
python manage.py runserver
