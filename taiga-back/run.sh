#!/usr/bin/env bash

set -ex

# Running migrations
python manage.py migrate --noinput

# Can't add these to the docker image - they'd cause a massive security hole every time the container restarted
#python manage.py loaddata initial_user
#python manage.py loaddata initial_project_templates

python manage.py compilemessages
python manage.py collectstatic --noinput

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn taiga.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
