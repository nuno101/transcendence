# Use an official Python runtime as a parent image
FROM python:3.11-alpine3.18
RUN pip install --upgrade pip
RUN mkdir /app
WORKDIR /app
COPY conf/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN django-admin startproject transc 
COPY conf/settings.py /app/transc
WORKDIR /app/transc
# Run the application:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
