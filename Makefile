# Makefile
#!/bin/bash

start: 
	poetry run app

update:
	sudo apt update

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