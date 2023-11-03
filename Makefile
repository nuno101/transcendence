.PHONY: all build up clean re clean-all

all: build up

build:
	mkdir -p  $(HOME)/data/transcendence/volumes/C
	mkdir -p  $(HOME)/data/transcendence/volumes/D
	mkdir -p  $(HOME)/data/transcendence/volumes/E
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

clean: down
	docker system prune -f
	rm -rf $(HOME)/data/transcendence/volumes

re: clean all

clean-all:
	docker compose -f ./docker-compose.yml down --volumes --rmi all
	docker system prune -f --volumes -a
	rm -rf $(HOME)/data/transcendence/volumes