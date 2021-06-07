#!/bin/sh

echo "Starting Docker-Entrypoint.sh"

python manage.py migrate
python manage.py runserver 0.0.0.0:8000

exec "$@"