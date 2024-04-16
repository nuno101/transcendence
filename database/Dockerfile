FROM postgres:16.0-alpine3.18
RUN mkdir /mnt/postgres && chown postgres:postgres -R /mnt/postgres
COPY postgresql.conf /etc/postgresql.conf
RUN chown postgres:postgres /etc/postgresql.conf
CMD [ "postgres", "-c", "config_file=/etc/postgresql.conf" ]
