check: lint typecheck test

test:
	poetry run pytest

lint:
	poetry run flake8

typecheck:
	poetry run mypy .