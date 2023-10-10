FROM alpine:latest

# Install build dependencies
RUN apk --no-cache add \
        linux-headers \
        flex \
        bison \
        perl \
        wget \
        build-base \
        readline-dev \
        zlib-dev \
        libxml2-dev \
        libxslt-dev \
        openssl-dev

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Get PostgreSQL Source Code
RUN wget https://ftp.postgresql.org/pub/source/v13.4/postgresql-13.4.tar.gz && \
    tar -xf postgresql-13.4.tar.gz && \
    cd postgresql-13.4

# Build and Install PostgreSQL
WORKDIR postgresql-13.4
RUN ./configure && \
    make world && \
    make install

# Add postgres user and setup necessary paths
RUN adduser -D postgres && \
    mkdir -p /usr/local/pgsql/data && \
    chown -R postgres:postgres /usr/local/pgsql/data

USER postgres

# Initialize database
RUN /usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data

#"RUN initdb" enabling trust authentification TODOO??

# PostgreSQL default port
EXPOSE 5432



# Start PostgreSQL
CMD ["/usr/local/pgsql/bin/postgres", "-D", "/usr/local/pgsql/data"]
