all: build up

build:
	sudo mkdir -p  /home/$(USER)/data/transcendence/volumes/C
	sudo mkdir -p  /home/$(USER)/data/transcendence/volumes/D
	sudo mkdir -p  /home/$(USER)/data/transcendence/volumes/E
	sudo docker-compose -f ./docker-compose.yml build

up:
	sudo docker-compose -f ./docker-compose.yml up -d

clean:#Todoo! Add a smaller cleaner

clean-all:
# WARNING: Deleting images, volumes, files in host, everything will be gone.
	sudo docker-compose -f ./docker-compose.yml down --volumes --rmi all
	sudo docker system prune -f --volumes -a
	sudo rm -rf /home/$(USER)/data/transcendence/volumes/C /home/$(USER)/data/transcendence/volumes/D /home/$(USER)/data/transcendence/volumes/E