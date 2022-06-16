help:   ## show this message
	@cmd/show-help makefile | sort -V

build:   ## start app building first
	docker-compose up -d --build

start:   ## start app
	docker-compose up -d

stop:   ## stop app
	docker-compose down

.PHONY: help start stop
