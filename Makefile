run:
	python server.py
rebuild:
	docker-compose up -d --no-deps --force-recreate --build
alembic_create:
	alembic revision --autogenerate -m "Added tables"
alembic_upgrade:
	alembic upgrade head
alembic_rollback:
	alembic downgrade -1