#!/bin/bash
python github/manage.py migrate
python github/manage.py test user
python github/manage.py runserver 0.0.0.0:8081