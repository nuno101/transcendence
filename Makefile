.PHONY: all build up init migrate superuser ssl_create down blog documentation volume_clean docker_clean \
				docker_fclean data_clean clean fclean re test help
-include docker.mk

ENV_FILES	:= .env elastic-stack/.env
build up down volume_clean docker_fclean: $(ENV_FILES)

$(ENV_FILES):
	$(error missing file: $@. you can create one based on $@.sample)

all: build ssl_create up migrate

build:
	mkdir -p  $(HOME)/docker-data/transcendence/database
	mkdir -p  $(HOME)/docker-data/transcendence/backend
	mkdir -p  $(HOME)/docker-data/transcendence/redis
	docker compose build

up:
	docker compose up -d

init: migrate superuser

migrate:
	docker exec -it backend python3 manage.py makemigrations
	docker exec -it backend python3 manage.py makemigrations api 
	docker exec -it backend python3 manage.py migrate

superuser:
	docker exec -it backend python3 manage.py createsuperuser

ssl_create:
	mkdir -p .ssl
	(cd .ssl && sh ../tools/ssl_generate.sh ../conf/ssl_information.txt)

down:
	docker compose down

# follow backend logs
blog:
	docker logs -f backend

documentation:
	@echo "Changing directory to $(PWD)/tools"
	@(cd tools && sh generate_api_docs.sh)
	@echo "Working directory changed to $(PWD)"

volume_clean:
	docker compose down -v

docker_clean: down volume_clean
	docker system prune -f

docker_fclean: docker_clean
	docker compose -f ./docker-compose.yml down --volumes --rmi all

data_clean: volume_clean
	rm -rf  $(HOME)/docker-data/transcendence

ssl_clean:
	rm -rf .ssl

clean: docker_clean

fclean: docker_fclean data_clean ssl_clean

re: clean all

validate:
	@echo "Searching for files with endings that should not be in the repo"
	@find . -name "*.key" -print -quit && find . -name "*.crt" -print -quit

help:
	@echo "all: build up migrate"
	@echo "build: build the docker images"
	@echo "up: start the docker containers"
	@echo ""
	@echo "init: migrate superuser"
	@echo "migrate: run the migrations"
	@echo "superuser: create a superuser"
	@echo "ssl_create: create ssl credentials if they do not exist already"
	@echo "down: stop the docker containers"
	@echo ""
	@echo "blog: follow the backend logs"
	@echo "documentation: generate/update the API documentation"
	@echo ""
	@echo "volume_clean: remove all docker compose volumes"
	@echo "docker_clean: down & volume_clean & delete project docker containers"
	@echo "docker_fclean: docker_clean & delete project docker images"
	@echo "data_clean: volume_clean & delete project data folders on host"
	@echo "ssl_clean: remove existing ssl files"
	@echo ""
	@echo "clean: remove all docker compose containers and volumes"	
	@echo "fclean: remove all docker compose containers, volumes and images"
	@echo "re: clean all and start again"
	@echo ""
	@echo "help: show this message"
