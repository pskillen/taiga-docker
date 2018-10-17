# Taiga Back-end Docker Image

This Docker image helps you to run your own [Taiga](https://taiga.io) instance. It should be run in conjunction
with a suitable front end (e.g. [nhsmdu/taiga-front](https://hub.docker.com/r/nhsmdu/taiga-front/)) and a Postgres DB.

See the repository at https://github.com/pskillen/taiga-docker for full information

## Supported tags

* `3.4.5` from [taiga-back @ 3.5.4](https://github.com/taigaio/taiga-back/tree/3.4.5)

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

TODO
