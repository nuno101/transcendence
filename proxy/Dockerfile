FROM nginx:1.24-alpine3.17
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/
COPY kibana.conf /etc/nginx/conf.d/
RUN mkdir /mnt/nginx && touch /mnt/nginx/error.log /mnt/nginx/access.log
CMD ["nginx", "-g", "daemon off;"]
