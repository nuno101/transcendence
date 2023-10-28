.PHONY: all build up clean clean-all

all: build up

build:
	mkdir -p  $(HOME)/data/transcendence/volumes/C
	mkdir -p  $(HOME)/data/transcendence/volumes/D
	mkdir -p  $(HOME)/data/transcendence/volumes/E
	docker-compose -f ./docker-compose.yml build

up:
	docker-compose -f ./docker-compose.yml up -d

clean:#Todoo! Add a smaller cleaner

clean-all:
	docker-compose -f ./docker-compose.yml down --volumes --rmi all
	docker system prune -f --volumes -a
	rm -rf $(HOME)/data/transcendence/volumes
