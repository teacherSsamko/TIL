# How to solve m1 issue with Rossetta

## issue1: pip install failed on M1

Solution: Use Rosetta-terminal for pip installing [Ref](https://www.courier.com/blog/tips-and-tricks-to-setup-your-apple-m1-for-development/)

## issue2: postgresql in docker

Solution: Use `DOCKER_DEFAULT_PLATFORM` environment variable. [Ref](https://stackoverflow.com/questions/62807717/how-can-i-solve-postgresql-scram-authentifcation-problem)  
`export DOCKER_DEFAULT_PLATFORM=linux/amd64`
