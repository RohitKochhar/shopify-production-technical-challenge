#!/bin/bash

pip3 install -r requirements.txt

cd app
python manage.py makemigrations tracker
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000