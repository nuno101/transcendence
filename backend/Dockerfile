# Use an official Python runtime as a parent image
FROM python:3.11-alpine3.18
RUN pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

# Copy conf
RUN mkdir conf
COPY conf/ conf

RUN apk add build-base
RUN apk add libffi-dev
RUN pip install --no-cache-dir -r conf/requirements.txt

# Copy app
COPY transc transc
# updated allowed_ips and Postgres DB config
COPY conf/settings.py transc/transc/

# Django project skeleton
#RUN django-admin startproject transc 
# Django api app skeleton
# python manage.py startapp api

WORKDIR /app/transc

#FIXME: only for debugging
RUN apk add postgresql15-client

# Run the Django application:
CMD ["sh", "/app/conf/entrypoint.sh"]
