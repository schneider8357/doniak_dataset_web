#!/bin/sh

/usr/app/venv/bin/python manage.py migrate
/usr/app/venv/bin/gunicorn sits.wsgi --bind 0.0.0.0:8000 --worker-tmp-dir /dev/shm --workers=1 --threads=2 --worker-class=gthread --log-file=-
