# Docker-compose

## COMPOSE FILE with environment variable

`export COMPOSE_FILE=local.yml`

## run

Runs a one-time command against a service. For example, the following command starts the web service and runs bash as its command.  

`docker-compose run web bash`

### args

- `--rm`: Remove container after run. Ignored in detached mode.
