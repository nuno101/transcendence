all: build up

build:
	mkdir -p  /home/$(USER)/data/transcendence/volumes/C
	mkdir -p  /home/$(USER)/data/transcendence/volumes/D
	mkdir -p  /home/$(USER)/data/transcendence/volumes/E
	docker-compose -f ./docker-compose.yml build

up:
	docker-compose -f ./docker-compose.yml up -d

clean:#Todoo! Add a smaller cleaner

clean-all:
	docker-compose -f ./docker-compose.yml down --volumes --rmi all
	docker system prune -f --volumes -a
	sudo rm -rf /home/$(USER)/data/transcendence/volumes/*