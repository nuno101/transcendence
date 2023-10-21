.PHONY: all build rebuild run stop down clean re

all: build run

build:
	echo "Building Docker images..."
	docker build -t vuejs-transc .

run:
	docker run -it -p 8080:80 --rm --name hellovuejs vuejs-transc
