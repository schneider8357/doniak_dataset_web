# Doniak Dataset Web

Instructions for deploying

## Step 1: Build container using Dockerfile

```
docker build --no-cache -t doniak-dataset-django:latest .
```

## Step 2: Package image as a tarball

```
docker save --output image_doniak-dataset-django.tar.gz doniak-dataset-django:latest
```

## Step 3: Copy the tarball into the VM

```
scp image_doniak-dataset-django.tar.gz <user>@<hostname>:/tmp
```

## Step 4: Copy docker-compose.yaml into the VM

```
scp docker-compose.yaml <user>@<hostname>:~
```

## Step 5: Load the image into the local registry

Note: the following steps should be executed from within the VM.

```
docker load --input /tmp/image_doniak-dataset-django.tar.gz
```

## Step 6: Start the containers

```
docker-compose up -d
```

And then watch the logs for errors:
```
docker-compose logs -f
```