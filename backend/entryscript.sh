#!/bin/bash

mv /usr/src/* /var/lib/backend/data/

cd /var/lib/backend/data/app

echo -e '\n' | nest new test_project

cd test_project

npm run start:dev