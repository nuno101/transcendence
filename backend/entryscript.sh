#!/bin/bash

set -x

mv * ../var/lib/backend/data/

cd ../var/lib/backend/data

npm run start:dev

set +x
