#!/bin/bash

set -e

#docker build --no-cache -t doniak-dataset-django:latest .
docker build -t doniak-dataset-django:latest .
docker save --output image_doniak-dataset-django.tar.gz doniak-dataset-django:latest
scp image_doniak-dataset-django.tar.gz vm-doniak:/tmp
ssh vm-doniak docker load --input /tmp/image_doniak-dataset-django.tar.gz
ssh vm-doniak 'docker-compose -f /opt/doniak-dataset-web/docker-compose.yaml run --entrypoint "./manage.py migrate" backend'
ssh vm-doniak docker-compose -f /opt/doniak-dataset-web/docker-compose.yaml up -d --force-recreate
