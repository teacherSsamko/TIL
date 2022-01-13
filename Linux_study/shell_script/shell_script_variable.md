# Variables in shell script

## Arguments

- $0 - The name of the Bash script.
- $1 - $9 - The first 9 arguments to the Bash script. (As mentioned above.)
- $# - How many arguments were passed to the Bash script.
- $@ - All the arguments supplied to the Bash script.
- $? - The exit status of the most recently run process.
- $$ - The process ID of the current script.
- $USER - The username of the user running the script.
- $HOSTNAME - The hostname of the machine the script is running on.
- $SECONDS - The number of seconds since the script was started.
- $RANDOM - Returns a different random number each time is it referred to.
- $LINENO - Returns the current line number in the Bash script.

## Quote

- '': Single quotes will treat every character literally.
- "": Double quotes will allow you to do substitution (that is include variables within the setting of the value).

## Command substitution

- $(): The dollar sign character ($) is used to start a variable substitution.
- \`: The backtick character (\`) is used to start a command substitution.
- ${}: The brace character (}) is used to start a variable substitution.
- $[]: The left square bracket ([) is used to start a conditional substitution.
- example: `myvar=$( ls /etc | wc -l )`
