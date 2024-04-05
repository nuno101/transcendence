#!/bin/sh

set -e
set -x

# Run the initial commands
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    GRANT ALL PRIVILEGES ON DATABASE "$POSTGRES_DB" TO "$POSTGRES_USER";
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
EOSQL

if [ ! -f /.installed ]; then
   
   echo "host all all 0.0.0.0/0 md5
host all all ::/0 md5" >> /var/lib/postgresql/data/pg_hba.conf 
   apk update
   apk add curl
   touch /.installed
fi

if [ ! -f /.elk-installed ]; then
   curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.11.4-linux-x86_64.tar.gz
   tar xzvf filebeat-8.11.4-linux-x86_64.tar.gz
   #curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.13.0-darwin-x86_64.tar.gz
   #tar xzvf filebeat-8.13.0-darwin-x86_64.tar.gz
   #touch /.elk-installed
fi

set +x
