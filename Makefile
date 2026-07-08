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

create_post:
	uv run manage.py create_post --title "$(title)" --content "$(content)"

delete_post:
	uv run manage.py delete_post --post_id $(id)

update_post:
	uv run manage.py update_posts --id $(id) --title "$(title)"

test:
	uv run manage.py test
