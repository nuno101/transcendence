FROM node:14.17.1-alpine

WORKDIR /app

COPY ./backend/tools/entrypoint.sh /app/

RUN apk update && apk add bash

EXPOSE 3000

CMD ["bin/sh", "entrypoint.sh"] 