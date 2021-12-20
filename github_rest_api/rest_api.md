# github rest api

## Get User info

`curl -i https://api.github.com/users/teacherSsamko`

## Get repo info

`curl -i https://api.github.com/repos/teacherSsamko/TIL`

- use authentication

`curl -i -H "Authoriziation: token {git access token}" https://api.github.com/user`

- get latest release

`curl -i https://api.github.com/repos/teacherSsamko/TIL/releases/latest`
