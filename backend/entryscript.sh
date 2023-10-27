#!/bin/bash

mv /usr/src/app/* /var/lib/backend/data/

cd /var/lib/backend/data/

echo -e '\n' | nest new test_project

cd test_project

apt update

apt list --upgradable

npx prisma init

#npx prisma generate

npm run start

npx prisma db pull
