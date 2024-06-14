SLU
===

## Requirements

- [Docker (18.06.0+)](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Django Style Guide

We follow [HackSoftware's Django Style Guide](https://github.com/HackSoftware/Django-Styleguide)
to create scalable and testable Django code.

The most important concept is [Services](https://github.com/HackSoftware/Django-Styleguide#services)
where the business logic lives.

## Setup

Make a copy of `.env.example` named `.env` and adjust the values accordingly.

```bash
$ cp .env.example .env
```

Build and run containers.

```bash
$ docker-compose build
$ docker-compose up -d
```

## Creating and running Django database migrations

Use the pre-configured scripts when running `migrate` and `makemigrate`.

```bash
$ docker-compose run --rm base makemigrations
$ docker-compose run --rm base migrate
```

If you have `make` installed:

```bash
$ make migrations
$ make migrate
```

You can check `Makefile` for other options.

## Running Django commands

You can execute django manage.py commands inside the container:

```bash
$ docker-compose exec <service_name> python manage.py <command>
```

Example: Creating a superuser.

```bash
$ docker-compose exec core python manage.py createsuperuser
```

## Accessing the services

SLU Services

- Core - http://localhost:8000
- Payment - http://localhost:8001
- Audit Trail
- Notification

REST API Docs can be access via `/docs` url of each service.

- Core API Docs - http://localhost:8000/docs
- Payment API Docs - http://localhost:8001/docs

Django Admin can be accessed via `slu/core` service

- Django Admin - http://localhost:8000/admin
