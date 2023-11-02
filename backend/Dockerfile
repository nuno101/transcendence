# Use an official Python runtime as the parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE django_backend.settings
ENV POSTGRES_DB ${POSTGRES_DB}
ENV POSTGRES_PASSWORD ${POSTGRES_PASSWORD}
ENV POSTGRES_USER ${POSTGRES_USER}
ENV POSTGRES_URL ${POSTGRES_URL}

# Set the working directory in the container
WORKDIR /usr/src/app

# Install the required dependencies with pip
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY ./django_backend/ ./django_backend
COPY ./*.py ./

RUN ls -al /usr/src/app

# Expose port 8000 to the outside world
EXPOSE 3000

# Run the WSGI server using gunicorn on port 3000
#CMD ["ls", "-al", "/usr/src/app/django_backend"]

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "django_backend.wsgi:application"]