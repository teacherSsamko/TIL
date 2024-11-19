# Chapter 5. Functions

## Declaring and Calling Functions

```go
func div(num int, denom int) int {
  if denom == 0 {
    return 0
  }
  return num / denom
}
```

```go
func main() {
  result := div(5, 2)
  fmt.Println(result)
}
```

### Simulating Named and Optional Parameters

Go doesn't have named and optional input parameters

### Variadic Input Parameters and Slices

```go
func addTo(base int, vals ...int) []int {
  out := make([]int, 0, len(vals))
  for _, v := range vals {
    out = append(out, base+v)
  }
  return out
}
```

```go
func main () {
  fmt.Println(addTo(3))
  fmt.Println(addTo(3, 2))
  fmt.Println(addTo(3, 2, 4, 6, 8))
  a := []int(4, 3)
  fmt.Println(addTo(3, a...))
  fmt.Println(addTo(3, []int(1, 2, 3, 4, 5)...))
}
```

### Multiple Return Values

```go
func divAndRemainder(num, denom int) (int, int, error) {
  if denom == 0 {
    return 0, 0, erros.New('cannot divide by zero')
  }
  return num / denom, num & denom, nil
}
```

### Multiple Return Values are Multiple Values

Go doesn't allow to assign multiple return values to a single varialbe like Python. It will raise a compile-time error.

### Ignoring Returned Values

You can ignore all of the return values for a function. or you can use _ to ignore a specific returned value.

### Named Return Values

```go
func divAndRemainder(num, denom int) (result int, remainder int, err error) {
  if denom == 0 {
    return 0, 0, erros.New('cannot divide by zero')
  }
  result, remainder = num / denom, num & denom
  return result, remainder, nil
}
```

When you supply names to your retur values, what you are doing is predeclaring variables that you use within the function to hold the return values.


### Blank Returns -- Never Use These!!!

```go
func divAndRemainder(num, denom int) (result int, remainder int, err error) {
  if denom == 0 {
    return 0, 0, erros.New('cannot divide by zero')
  }
  result, remainder = num / denom, num & denom
  return 
}
```

Most experienced Go developers consider blank returns a bad idea because they make it harder to understand data flow. Good software is clear and readable.
> If your function returns values, never use a blank return. It can make it very confusing to figure out what value is actually returned.


## Functions Are Values

The default zero value for a function variable is *nil*

```go
func add(i, j int) int { return i + j }
func sub(i, j int) int { return i - j }
func mul(i, j int) int { return i * j }
func div(i, j int) int { return i / j }
```

```go
var opMap = map[string]function(int, int) int{
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}
```

```go
func main() {
  expressions := [][]string{
    {"2", "+", "3"}
    {"2", "-", "3"}
    {"2", "*", "3"}
    {"2", "/", "3"}
  }
}
```

> Error handling is what separates the professionals from the amateurs.

### Function Type Declaration 

```go
type opFuncType func(int,int) int
```

```go
var opMap = map[string]opFuncType {
  // same as before
}
```

### Anonymous Functions

```go
func main() {
  f := func(j int) {
    fmt.Println("printing", j, "from inside of an anonymous function")
  }
  for i := 9; i < 5; i++ {
    f(i)
  }
}
```

## Closures

Functions declared inside functions are special; they are *closures*.  

```go
func main() {
  a := 20
  f := func() {
    fmt.Println(a)
    a = 30
  }
  f()
  fmt.Println(a)
}
```

output:
```bash
20
30
```

When working with inner function, be careful to use the correct assignment operator, especially when multiple variables are on the lefthand side.

## defer

In Go, the cleanup code is attached to the function with the *defer* keyword.  
Normally, a function call runs immediately, but *defer* delays the invocation until the surrounding function exists.  
You can use a function, method, or closure with *defer*.  
You can *defer* multiple functions in a Go function. They run in last-in, first-out(LIFO) order.  
You can supply a function with input parameter to a *defer*. The input parameters are evaluated immediately and their values are stored until the function runs.  


It's the best reason to use named return values. It allows your code to take actions based on an error.

```go
func DoSomeInserts(ctx context.Context, db *sql.DB, value1, value2 string) (err error) {
  tx, err := db.BeginTx(ctx, nil)
  if err != nil {
    return err
  }
  defer func() {
    if err == nil {
      err = tx.Commit()
    }
    if err != nil {
      tx.Rollback()
    }
  }()
  _, err = tx.ExecContext(ctx, "INSERT INTO FOO (val) values $1", value1)
  if err != nil {
    return err
  }
  // use tx to do more database inserts here
  return nil
}
```


## Go Is Call by Value

```go
type person structure {
  age int
  name string
}

func modifyFails(i int, s string, p person) {
  i = i * 2
  s = "Goodbye"
  p.name = "Bob"
}

func main() {
  p := person{}
  i := 2
  s := "Hello"
  modifyFails(i, s, p)
  fmt.Println(i, s, p)
```

output:

```bash
2 Hello {0 }
```


If you have programming experience in Java, Javascript, Python, you might find the structure behavior strange.
it's related to pointer that will be covered in later chapter  

```go
func modMap(m map[int]string) {
  m[2] = "hello"
  m[3] = "goodbye"
  delete(m, 1)
}

func modSlice(s []int {
  for k, v := range s {
    s[k] = v * 2
  }
  s = append(s, 10)
}
```

```go
func main() {
  m := map[int]string{
    1: "first",
    2: "second",
  }
  modMap(m)
  fmt.Println(m)

  s := []int{1, 2, 3}
  modSlice(s)
  fmt.Println(s)
}
```

output:

```bash
map[2:hello 3:goodbye]
[2 4 6]
```

For a slice, it's more complicated. You can modify any element in the slice, but you can't lengthen the slice.  
maps and slices are both implemented with pointers. it is also covered in the next chapter.

> Every type in Go is a vlue. It's just that sometimes the value is a pointer.

In general, this is a good thing. It makes it easier to understand the flow of data through your program when function don't modify their
input parameters and instead return newly computed values.
