ARG STACK_VERSION
FROM docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}
COPY ilm_transcendence.json /usr/share/elasticsearch/config/
COPY start.sh /usr/local/bin/
CMD [ "start.sh" ]
