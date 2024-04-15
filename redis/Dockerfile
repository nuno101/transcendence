FROM redis:7.2.4
COPY redis.conf /usr/local/etc/redis/redis.conf
RUN mkdir /mnt/redis && touch /mnt/redis/redis.log && chown redis:redis -R /mnt/redis/
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
