FROM alpine:3.17
RUN apk add --upgrade apk-tools && apk upgrade --available
RUN apk add nodejs npm
WORKDIR /app
COPY package.json ./
COPY vite.config.js ./
COPY .eslintrc.cjs ./
COPY .prettierrc.json ./
COPY index.html ./
RUN npm install
CMD ["npm", "run", "dev"]
