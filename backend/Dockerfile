FROM node:16.20.2

WORKDIR /usr/src/app

COPY ./nestjs-dockerized/package*.json ./

RUN npm install

COPY ./nestjs-dockerized/. .

RUN npm run build

CMD ["node", "dist/main"]