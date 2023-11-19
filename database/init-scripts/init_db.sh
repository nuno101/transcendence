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
   touch /.installed
fi

set +x
