help:   ## show this message
	@cmd/show-help makefile | sort -V

env:	## generar ambiente de desarrollo
	virtualenv .venv
	. .venv/bin/activate
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

build:   ## start app building first
	docker-compose -f containers/dev/compose.yml up -d --build

start:   ## start app
	docker-compose -f containers/dev/compose.yml up -d

stop:   ## stop app
	docker-compose -f containers/dev/compose.yml down

logs:   ## show app logs
	docker-compose -f containers/dev/compose.yml logs -f

test:	## generar ambiente de desarrollo
	. .venv/bin/activate
	pytest
	pre-commit run --all

.PHONY: help start stop test
