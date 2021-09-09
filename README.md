# recipe-app-api

Recipe app api source code.

## commands start project in docker container

docker-compose run app sh -c "django-admin.py startproject app ."

## Run docker

`$ docker build .`

## Run docker compose

`$ docker-compose build`

# TDD in django

Django looks for tests name file or folder in app folder for execute tests.

`$ docker-compose run app sh -c "python manage.py test"`

For linting:
`$ docker-compose run app sh -c "python manage.py test && flake8"`

# Test driven development (TDD)

When you write the test before you write the code.

# Core app

Create a core app that centralize all migrations and thing which can be used into sub apps.
`$ docker-compose run app sh -c "python manage.py startapp core"`

# Create Migration based on model

When you change de model, you must run this command again.

`$ docker-compose run app sh -c "python manage.py makemigrations <appname>"`
