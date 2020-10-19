#!/bin/bash
.PHONY: default
.SILENT:


default:

shell:
	docker-compose stop api
	docker-compose run --rm --service-ports api bash

createsuperuser:
	docker-compose run --rm api python manage.py createsuperuser

createsuperuserfast:
	docker-compose run --rm api python manage.py createsuperuserfast --username admin --password vessel1234 --noinput --email 'admin@email.com'

migrations:
	docker-compose run --rm api python manage.py makemigrations

migrate:
	docker-compose run --rm api python manage.py migrate --noinput

start:
	docker-compose up -d

start_api:
	docker-compose run --rm --service-ports api

stop:
	docker-compose down

collectstatic:
	docker-compose run --rm api python manage.py collectstatic --noinput

build:
	docker-compose build --force-rm --no-cache --pull
	make collectstatic
	make tests

setup:
	docker network create vessel_net
	docker-compose build --force-rm --no-cache --pull
	make migrate
	make createsuperuserfast
	make collectstatic
	make tests

logs:
	docker-compose logs --follow

tests:
	docker-compose run --rm api python manage.py test vessel_api.vessels.tests vessel_api.equipments.tests

clean:
	make stop
	docker image rm $$(docker image ls -q -f reference=vessel_django_api)
	docker volume rm $$(docker volume ls -q -f name=vessel_api)
	docker network rm vessel_net

startapp:
	docker-compose stop api
	docker-compose run --rm api python manage.py startapp $(app)
	mv -f $(app) vessel_api/
	touch vessel_api/$(app)/serializers.py
	touch vessel_api/$(app)/choices.py
	touch vessel_api/$(app)/routers.py
	touch vessel_api/$(app)/services.py
