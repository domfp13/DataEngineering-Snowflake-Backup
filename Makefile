# -*- coding: utf-8 -*-
# Created by Luis Enrique Fuentes Plata

SHELL = /bin/bash

.PHONY: setup
setup: ## Build image
	@ echo "**********Building image**********"
	docker image build --rm -t dbt-runner .
	@ echo "**********Cleaning old version **********"
	docker image prune -f

.PHONY: build
build: ## docker-compose up
	@ echo "spinning up containers"
	docker-compose up -d

.PHONY: start
start: ## setup and build containers
	@ echo "Creating and Starting services"
	@ $(MAKE) setup
	@ $(MAKE) build

.PHONY: stop
stop: ## stop and destroy services
	@ echo "Removing services"
	docker-compose down

.PHONY: run-code-windows
run-code-w: ## Run main.py in Windows Git-Bash
	@ echo "Running python main"
	winpty docker exec -it docker-agent bash -c "python /usr/src/app/src/main.py"

.PHONY: run-code-linux
run-code-l: ## Run main.py in Unix System
	@ echo "Running"
	docker exec -it docker-agent bash -c "python /usr/src/app/src/main.py"

help: ## display this help message
	@ echo "Please use \`make <target>' where <target> is one of"
	@ perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
