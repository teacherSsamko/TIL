## Your First Go Program

### Making a go Module

```
$ mkdir ch1 && cd ch1
$ go mod init hello_world
```

These commands will create *go.mod* file looks like

```go
module hello_world

go 1.21
```

### go build

`$ touch hello.go`

```go
package main

import "fmt"

func main() {
fmt.Println("Hello, World!")
}
```

`$ go build`

`$ ./hello_world`

If you want to compile the code to a binary called "hello", 
`$ go build -o hello`

### go fmt

`$ go fmt ./...`

Using ./... tells a Go tool to apply the command to all the files in the current directory and all subdirectories.

If you open up *hello.go*, you'll see that the line with `fmt.Println` is now properly indented with a single tab.

> Remember to run `go fmt` before you compile your code. 
> So you don't hide logic changes in an avalanche of formatting changes.

## Staying Up-to-Date

Go programs compile to a standalone native binary, so you don't need to worry that updatiing your development environment could cause your currently deployed programs to fail.
