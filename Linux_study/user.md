# User

## add user Using user data file

<https://www.tecmint.com/create-multiple-user-accounts-in-linux>

## Commands - on Ubuntu

- check user id
  `id [username]`
- adduser
  `sudo adduser [username]`
- Add user to sudo group
  `sudo usermod -aG sudo [username]`
- change UID
  `sudo usermod -u [UID] [username]`
- change GID
  `sudo usermod -g [GID] [username]`
- remove user
  `sudo deluser --remove-home [username]`
- remove user from sudo group
  `sudo deluser [username] sudo`
  - backup before removing user account
    `sudo deluser --remove-home --backup-to [backup dir path] [username]`
