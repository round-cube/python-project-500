install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
#	poetry build
	python3 -m pip install --force-reinstall --user dist/*.whl
#	poetry run flake8 gendiff

make lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest 
	poetry run coverage xml

#.PHONY: gendiff