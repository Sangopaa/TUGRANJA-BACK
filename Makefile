include .env

up:
	docker compose up

up_detached:
	docker compose up -d

create_db:
	docker compose exec -T tu-granja-db mysql -h tu-granja-db -uroot -p${MYSQL_DATABASE_PASSWORD} -e 'CREATE DATABASE `${MYSQL_DATABASE_DB}`'

run_migrations:
	docker compose exec -it app alembic upgrade head

create_migration:
	docker compose exec -it app alembic revision --autogenerate -m "${message}"

stop:
	docker compose stop

clean: stop
	docker container prune -f
	docker image rm tu-granja-image

clean_all: clean
	docker system prune -a
	docker volume rm tu-granja-volume

