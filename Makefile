run:
	uv run manage.py runserver

lint:
	uv run pre-commit run --all-files

migrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

superuser:
	uv run manage.py createsuperuser
