#!/bin/bash

set -e

#docker build --no-cache -t doniak-dataset-django:latest .
docker build -t doniak-dataset-django:latest .
docker save --output image_doniak-dataset-django.tar.gz doniak-dataset-django:latest
scp image_doniak-dataset-django.tar.gz vm-doniak:/tmp
OLD_IMAGE_ID=$(ssh vm-doniak docker image inspect doniak-dataset-django:latest | jq -r .[0].Id | cut -d ":" -f 2)
ssh vm-doniak docker load --input /tmp/image_doniak-dataset-django.tar.gz
ssh vm-doniak 'docker-compose -f /opt/doniak-dataset-web/docker-compose.yaml run --rm --entrypoint "./manage.py migrate" backend'
ssh vm-doniak docker-compose -f /opt/doniak-dataset-web/docker-compose.yaml up -d --force-recreate
ssh vm-doniak docker image rm -f $OLD_IMAGE_ID
