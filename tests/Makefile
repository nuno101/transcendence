.PHONY: all build run re

all:
	echo "Robot testing Framework"

build:
	docker build -t transc-robotfw .

run:
	docker run -it --rm --network=host -v $(HOME)/projects/h42/projects/77_trans/tests:/tests transc-robotfw bash -c "robot --outputdir /tests/results  /tests/tests"
