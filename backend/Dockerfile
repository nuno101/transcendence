# Use an official Python runtime as a parent image
FROM python:3.11-alpine3.18
RUN pip install --upgrade pip
RUN mkdir /app
WORKDIR /app
COPY conf/requirements.txt /app/

RUN apk add build-base
RUN apk add libffi-dev
RUN pip install --no-cache-dir -r requirements.txt

# Django project skeleton
#RUN django-admin startproject transc 
# Django api app skeleton
# python manage.py startapp api

WORKDIR /app/transc
COPY transc /app/transc
# updated allowed_ips and Postgres DB config
COPY conf/settings.py /app/transc

#FIXME: only for debugging
RUN apk add postgresql15-client

# Run the Django application:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
