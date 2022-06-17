help:   ## show this message
	@cmd/show-help makefile | sort -V

env:	## generar ambiente de desarrollo
	virtualenv .venv
	. .venv/bin/activate
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

build:  ## build images
	docker-compose -f containers/dev/compose.yml build
	docker-compose -f containers/prod/compose.yml build

dev:   ## start development app
	docker-compose -f containers/dev/compose.yml up -d --build

prod:   ## start staging environment
	docker-compose -f containers/prod/compose.yml up -d --build

stop:   ## stop app
	docker-compose -f containers/dev/compose.yml down
	docker-compose -f containers/prod/compose.yml down

logs-dev:   ## show app logs for dev
	docker-compose -f containers/dev/compose.yml logs -f

logs-prod:   ## show app logs for staging
	docker-compose -f containers/prod/compose.yml logs -f

test:	## generar ambiente de desarrollo
	. .venv/bin/activate
	pytest
	pre-commit run --all

.PHONY: help start stop test
