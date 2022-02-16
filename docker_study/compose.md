# Docker-compose

## COMPOSE FILE with environment variable

`export COMPOSE_FILE=local.yml`

## run

Runs a one-time command against a service. For example, the following command starts the web service and runs bash as its command.  

`docker-compose run web bash`

### args

- `--rm`: Remove container after run. Ignored in detached mode.

### yml

- `ports`: Expose a container's ports to the host.
  - example: "8000:8888" means that the container's port 8000 will be exposed to the host's port 8888.
