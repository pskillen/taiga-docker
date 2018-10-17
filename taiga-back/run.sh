#!/usr/bin/env bash

set -ex

# Running migrations
python manage.py migrate --noinput
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn taiga.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
