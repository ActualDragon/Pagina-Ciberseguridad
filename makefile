help:   ## show this message
	cmd/show-help makefile

start:   ## start app
	docker-compose up -d

stop:   ## stop app
	docker-compose down

.PHONY: help start stop
