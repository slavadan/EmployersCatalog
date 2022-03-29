#!/bin/sh


sleep 10

cd /home/slavadan/docker

su -m myuser -c "python manage.py makemigrations"

su -m myuser -c "python manage.py migrate"

su -m myuser -c "python manage.py seed catalog --number=15"

su -m myuser -c "python manage.py runserver 0.0.0.0:8000"