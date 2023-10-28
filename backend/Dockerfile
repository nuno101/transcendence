FROM node:latest

WORKDIR /usr/src/app

COPY ./nestjs-dockerized/package*.json ./

RUN npm install -g npm@10.2.1

COPY ./nestjs-dockerized/. .


#DEbug tools
#RUN npm install postgresql-client --save
#---------------------------------------

#Prisma
RUN npm install --save-dev prisma
RUN npm install @prisma/client
RUN npx prisma init
COPY ./schema.prisma prisma/
COPY .env .

#need scripts because first npm build
#RUN npx prisma migrate dev --name init
#RUN npx prisma generate

RUN npm run build

CMD ["node", "dist/main"]