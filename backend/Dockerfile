FROM alpine:3.17

RUN mkdir -p backend/app

RUN apk add --update \
    nodejs \
    npm 

WORKDIR /backend/app

COPY package.json /backend/app

RUN npm install

COPY tools/start.sh /backend/app/start.sh
RUN chmod +x /backend/app/start.sh

ENTRYPOINT ["sh"]

CMD ["npm", "start"]