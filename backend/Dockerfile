FROM node:16.20.2

WORKDIR /usr/src/app

COPY ./package*.json ./

RUN npm install

RUN npm i -g @nestjs/cli

COPY ./entryscript.sh ./script.sh

RUN chmod 755 ./script.sh

CMD ["./script.sh"]
