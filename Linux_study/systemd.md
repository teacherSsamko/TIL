# systemd

## [Unit]

Units are the objects that `systemd` knows how to manage.

### Types of Units

- .target: A target unit is used to provide synchronization points for other units when booting up or changing states.

## [Service]

The [Service] section is used to provide configuration that is only applicable for services.

### Types of Services

- forking: This service type is used when the service forks a child process, exiting the parent process almost immediately. This tells `systemd` that the process is still running even though the parent exited.

## [Install]

This section is optional and is used to define the behavior or a unit if it is enabled or disabled.

- WantedBy: This is used to specify the target unit that this unit should be enabled for.
