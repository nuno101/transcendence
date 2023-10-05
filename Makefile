all: build up

build:
	sudo mkdir -p  /home/$(USER)/data/transcendence/volumes/C
	sudo mkdir -p  /home/$(USER)/data/transcendence/volumes/D
	sudo docker-compose -f ./docker-compose.yml build

up:
	sudo docker-compose -f ./docker-compose.yml up -d

clean:#Todoo!

clean-all:
# WARNING: Deleting images, volumes, files in host, everything will be gone.
	sudo docker-compose -f ./docker-compose.yml down --volumes --rmi all
	sudo docker system prune -f --volumes -a
	sudo rm -rf /home/$(USER)/data/transcendence/volumes/C
	sudo rm -rf /home/$(USER)/data/transcendence/volumes/D