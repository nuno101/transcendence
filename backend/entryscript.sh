#!/bin/bash

set -x

mv * ../var/lib/backend/data/

cd ../var/lib/backend/data

echo -e '\n' | npx @nestjs/cli new project_test

cd project_test
# Install project dependencies
npm install

#echo "start installation of typeorm" 
#
#npx typeorm migration:generate -n migration_test
#npx typeorm migration:generate -n MyMigration

#
#npx typeorm migration:run

npm run start:dev

set +x
