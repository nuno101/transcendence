FROM alpine:3.17

RUN mkdir -p /backend/app

RUN apk add --update \
    nodejs \
    npm 

WORKDIR /backend/app

COPY package.json /backend/app

RUN npm install

COPY . /app

CMD ["npm", "start"]