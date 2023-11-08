# Use an official Python runtime as a parent image
FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

WORKDIR /usr/src/app/django_docker/django_backend/

# Run the application:

#CMD ["tail", "-f", "/dev/null"] debug
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["python3", "manage.py", "runserver"] doesnt work?? get wrong ip... weird maybe change /etc/hosts