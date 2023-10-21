FROM node:18

WORKDIR /app

COPY ./package*.json /app/

RUN npm install -g @nestjs/cli

RUN npm install @nestjs/typeorm typeorm pg

RUN npm audit fix

COPY . .

RUN chmod 755 entryscript.sh

CMD ["./entryscript.sh"]
