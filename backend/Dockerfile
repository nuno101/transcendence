FROM node:18

WORKDIR /app

COPY ./package.json /app/

COPY ./package-lock.json /app/

RUN npm install -g @nestjs/cli

RUN npm install -g npm@10.2.0

RUN npm install @nestjs/typeorm typeorm pg

RUN npm audit fix

COPY . /app

EXPOSE 3000

RUN chmod 777 ./entryscript.sh

CMD ["bash", "./entryscript.sh"]
