FROM node:latest

WORKDIR /usr/src/app

COPY ./nestjs-dockerized/package*.json ./

RUN npm install -g npm@10.2.1

COPY ./nestjs-dockerized/. .

#Prisma
RUN npm install --save-dev prisma
RUN npm install @prisma/client
RUN npx prisma init
COPY ./schema.prisma prisma/
COPY .env .

#need scripts because first npm build or is it dist/main?
#RUN npx prisma migrate dev --name init
#RUN npx prisma generate

RUN npm run build

CMD ["node", "dist/main"]