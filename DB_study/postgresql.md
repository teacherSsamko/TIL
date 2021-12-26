# postgresQL

## issues

| The data directory was initialized by PostgreSQL version 12, which is not compatible with this version 14.1.  
`brew postgresql-upgrade-database`

## on Mac

- execute postgresql
  - `psql <user>` ex) `psql postgres`
- if you don't have user postgres(default user)
  - `/usr/local/opt/postgres/bin/createuser -s postgres`
- show all databases
  - `psql -l`

## Commands in postgresql terminnal

- `\du`: show database users
