# Makefile
#!/bin/bash

start:
	export TELEGRAM_API_TOKEN="5233294778:AAHXwcHCYIxTFKXYdiD3WAfGqzH89o1TLYc" && \
	export MONOBANK_API_TOKEN="uVcD_1lQRFNxhPAEYkE5fgIFr3FNVINHh4vu3TfCtyuE" && \
	export TELEGRAM_PROXY_URL="http://185.112.12.31:2831" && \
	export TELEGRAM_PROXY_LOGIN="nyckolaswork5" && \
	export TELEGRAM_PROXY_PASSWORD="gtbSCMaj" && \
	poetry run python app.py

update:
	sudo apt update && poetry update

install:
	poetry install

test:
	poetry run pytest app

test-coverage:
	poetry run pytest --cov=app --cov-report xml

lint:
	poetry run flake8 app

selfcheck:
	poetry check

check: selfcheck test-coverage lint

build:
	poetry build

package-install:
	pip install --user dist/*.whl


# Makefile last line
# ignores existing files
.PHONY: install test lint selfcheck check build