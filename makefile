help:   ## show this message
	@cmd/show-help makefile | sort -V

env:	## generar ambiente de desarrollo
	virtualenv .venv
	. .venv/bin/activate
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

build:   ## start app building first
	docker-compose up -d --build

start:   ## start app
	docker-compose up -d

stop:   ## stop app
	docker-compose down

test:	## generar ambiente de desarrollo
	. .venv/bin/activate
	pytest

.PHONY: help start stop test
