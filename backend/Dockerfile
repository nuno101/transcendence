FROM node:18

WORKDIR /app

COPY ./package.json /app/

COPY ./package-lock.json /app/

RUN npm install -g @nestjs/cli

RUN npm install

RUN npm fund

COPY . /app

EXPOSE 3000

RUN chmod 777 ./entryscript.sh

CMD ["bash", "./entryscript.sh"]
