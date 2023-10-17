FROM node:18

WORKDIR /app

COPY ./package.json /app/

COPY ./package-lock.json /app/

RUN npm install -g @nestjs/cli

RUN npm install

RUN npm fund

COPY . /app

EXPOSE 3000

CMD ["npm", "run", "start:dev"] 
