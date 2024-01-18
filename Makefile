.PHONY: all build up clean re clean-all

all: build up

build:
	mkdir -p  $(HOME)/data/transcendence/volumes/E
	docker compose build

up:
	docker compose up -d

init: migrate superuser

migrate:
	docker exec -it backend python3 manage.py makemigrations
	# TODO: Figure out why api app isn't updated automatically
	docker exec -it backend python3 manage.py makemigrations api 
	docker exec -it backend python3 manage.py migrate

superuser:
	docker exec -it backend python3 manage.py createsuperuser

down:
	docker compose down

clean: down
	docker system prune -f
	docker volume rm database_device -f
	rm -rf $(HOME)/data/transcendence/volumes

re: clean all

#clean-all:
#	docker compose -f ./docker-compose.yml down --volumes --rmi all
#	docker system prune -f --volumes -a
#	rm -rf $(HOME)/data/transcendence/volumes
