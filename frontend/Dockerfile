# build stage
#FROM node:lts-alpine as build-stage
#WORKDIR /app
FROM alpine:3.17 as build-stage
RUN apk add --upgrade apk-tools && apk upgrade --available
RUN apk add nodejs npm
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

#FROM alpine:3.17
#RUN apk add --upgrade apk-tools && apk upgrade --available
#RUN apk add nodejs npm
#WORKDIR /app
#RUN npm create vue@latest
#RUN cd transc
#RUN npm install

#EXPOSE 5173
#CMD ["npm", "run", "dev", "--host"]

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
