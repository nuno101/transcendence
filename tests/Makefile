.PHONY: all build run re

all: build run

build: .build

.build:
	docker build -t transc-robotfw .
	touch .build

run:
	docker run -it --rm --network=host -v .:/tests transc-robotfw bash -c "robot --outputdir /tests/results  /tests/tests"
