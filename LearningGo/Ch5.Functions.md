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
