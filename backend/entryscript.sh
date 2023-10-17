#!/bin/bash

echo -e '\n' | npx @nestjs/cli new project_test

cd project_test

# Install project dependencies
npm install

npm run start:dev