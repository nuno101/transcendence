# Use Alpine Linux as the base image
FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Create the directory for your application code
RUN mkdir -p /app/

# Copy your application code into the container
COPY ./src/index.js /app/index.js

# Set the permissions of the copied file (755 for executable)
RUN chmod 755 /app/index.js

# Copy package.json and package-lock.json from your project directory into the container
COPY package.json /app/package.json

RUN npm install

# Copy the generated package-lock.json into the /app directory
#RUN cp package-lock.json /app/package-lock.json
#RUN chmod 755 /app/package-lock.json

# Specify the command to start your application
CMD ["npm", "start"]
