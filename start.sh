#!/bin/bash
python github/manage.py makemigrations
python github/manage.py migrate
python github/manage.py test user repository milestone label
python github/manage.py runserver 0.0.0.0:8081