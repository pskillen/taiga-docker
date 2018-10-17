# Taiga Docker Images

These Docker containers help you to run your own [Taiga](https://taiga.io) instance.

See the repository at https://github.com/pskillen/taiga-docker for full information

Files:

* [Front end](taiga-front/)
* [Back end](taiga-front/)
* [docker-compose](docker-compose.yaml)

## Building

You must set the `TAIGA_VERSION` env var **AND** build arg to the name of the tag you want to build (minus any `-stable`
modifiers - these are applied by the relevant `Dockerfile`)

```
# NB: set env var AND build arg!
export TAIGA_VERSION=3.4.5
docker-compose build --build-arg TAIGA_VERSION=3.4.5
```

## Maintainer Info

This repository is maintained by [Patrick Skillen](https://github.com/pskillen) on behalf of NHS Scotland's [Medical
Devices Unit](https://www.medicaldevicesunit.org/)

The initial work for these images was based heavily on the work at https://github.com/ipedrazas/taiga-docker
