.PHONY: all build up init migrate superuser down documentation clean re blog
-include docker.mk

all: build up

build:
	mkdir -p  $(HOME)/data/transcendence/volumes/E
	mkdir -p  $(HOME)/docker-data/transcendence/redis
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

documentation:
	@echo "Changing directory to $(PWD)/tools"
	@(cd tools && sh generate_api_docs.sh)
	@echo "Working directory changed to $(PWD)"

docker_clean: down
	docker system prune -f
	docker volume rm database_device -f
	docker volume rm redis_device -f

data_clean:
	rm -rf $(HOME)/data/transcendence/volumes
	rm -rf  $(HOME)/docker-data/transcendence/redis

docker_fclean: docker_clean
	docker compose -f ./docker-compose.yml down --volumes --rmi all

clean: docker_clean data_clean

fclean: docker_fclean data_clean

re: clean all

# follow backend logs
blog:
	docker logs -f backend
