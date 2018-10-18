# Taiga Back-end Docker Image

This Docker image helps you to run your own [Taiga](https://taiga.io) instance. It should be run in conjunction
with a suitable front end (e.g. [nhsmdu/taiga-front](https://hub.docker.com/r/nhsmdu/taiga-front/)) and a Postgres DB.

See the repository at https://github.com/pskillen/taiga-docker for full information

## Supported tags

* `3.4.5-r5` from [taiga-back @ 3.5.4](https://github.com/taigaio/taiga-back/tree/3.4.5)

## Quick start

TODO:
* `docker run ...` command

TODO: Explain why we have to run the following manually...

```
# Inside the container
python manage.py loaddata initial_user
python manage.py loaddata initial_project_templates
```

Default credentials: **admin** / **123123**

## Compose file

See [here](https://github.com/pskillen/taiga-docker/blob/master/docker-compose.yaml) for the latest compose file

## Env vars

| Var | Required | Default | Info |
|---|---|---|---|
| DEBUG | No | False | See [Django DEBUG](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DEBUG) |
| SECRET_KEY | **Yes** |  | Must be set to a secure, random, **secret** value. See Django [SECRET_KEY](https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-SECRET_KEY) |
| DB_HOST | No | postgres |  |
| DB_PORT | No | 5432 |  |
| DB_NAME | No | taiga |  |
| DB_USER | No | postgres |  |
| DB_PASSWORD | No | (blank) |  |
| API_PUBLIC_PROTOCOL | No | http |  |
| API_PUBLIC_DOMAIN | No | localhost:8000 |  |
| FRONTEND_PUBLIC_PROTOCOL | No | http | Used to generate URLs in emails, etc |
| FRONTEND_PUBLIC_DOMAIN | No | localhost:8000 | Used to generate URLs in emails, etc |
| MEDIA_URL | No | http://localhost:8000/media/ | **Must** end with a / |
| STATIC_URL | No | http://localhost:8000/static/ | **Must** end with a / |
| DEFAULT_FROM_EMAIL | No | (empty) |  |
| EMAIL_USE_TLS | No | True |  |
| EMAIL_HOST | No | (empty) |  |
| EMAIL_PORT | No | (empty) |  |
| EMAIL_HOST_USER | No | (empty) |  |
| EMAIL_HOST_PASSWORD | No | (empty) |  |
| PUBLIC_REGISTER_ENABLED | No | False | Enable public registrations? |
| STATS_ENABLED | No | True |  |
| JIRA_IMPORTER_ACTIVE | No | False | See https://taigaio.github.io/taiga-doc/dist/setup-faqs.html |
| JIRA_CONSUMER_KEY | No | (empty) | Name of cert? |
| JIRA_PRIVATE_CERT | No | (empty) | Contents of private key file (not filename) |
| JIRA_PUBLIC_CERT | No | (empty) | Contents of public key file (not filename) |
