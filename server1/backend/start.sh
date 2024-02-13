#!/bin/bash
sleep 5
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py createsuperuser --noinput
gunicorn setup.wsgi:application --bind 0.0.0.0:8000