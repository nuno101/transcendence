ENV_FILE := .env
include $(ENV_FILE)
VOLUMES := $(BACKEND_VOLUME) $(DATABASE_VOLUME) $(FRONTEND_VOLUME)

.PHONY: all build up clean clean-all

all: build up

build:
	mkdir -p $(VOLUMES)
	docker-compose -f ./docker-compose.yml build

up:
	docker-compose -f ./docker-compose.yml up -d

clean:#Todoo! Add a smaller cleaner

clean-all:
	docker-compose -f ./docker-compose.yml down --volumes --rmi all
	docker system prune -f --volumes -a
	rm -rf $(VOLUMES)