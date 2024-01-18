# build stage
FROM python:3.12-alpine as build

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt


# runtime stage
FROM python:3.12-alpine

RUN apk add -y --no-cache curl

RUN addgroup -g 8000 python && \
    adduser -S -u 8000 -g python python

RUN mkdir /usr/app && mkdir /usr/app/media && mkdir /usr/app/static
RUN chown -R python:python /usr/app
WORKDIR /usr/app

COPY --chown=python:python --from=build /usr/app/venv ./venv
COPY --chown=python:python . .

USER 8000

ENV PATH="/usr/app/venv/bin:$PATH"
ENV PYTHONPATH="/usr/app:$PYTHONPATH"

ENTRYPOINT ["/usr/app/entrypoint.sh"]
