# Chapter 3. Composite Types

## Arrays - Too rigid to use directly

## Slices

Most of the time, when you want a data structure that holds a sequence of values, a slice is what you should use.  
In Go, *nil* is an identifier that represents the lack of a value for some types.  
A *nil* slice contains nothing.  
A slice is not comparable. The only thing you can compare a slice with using `==` is *nil*

`fmt.Println(x == nil)`

When you take a slice from a slice, you are not making a copy of the data. Instead, you now have two variables that are sharing memory.

To avoid complicated slice situations, you should either never use append with a subslice or make sure that append doesn't cause an overwrite 
by using a full slice expression.  

## Maps

### The comma ok idiom

A map returns the zero value if you ask for the value assoicated with a key that's not in the map.  
Go provides the comma ok idiom to tell the difference between a key that's associated with a zero value and a key that's not in the map

```go
n := map[string]int{
  "hello": 5,
  "world": 0,
}
v, ok := n["hello"]
fmt.Println(v, ok)

v, ok := n["world"]
fmt.Println(v, ok)

v, ok := n["goodbye"]
fmt.Println(v, ok)
```

```
5 true
0 true
0 false
```

## Structs

> Go doesn't have classes, because it doens't have inheritance.

### Anonymous Structs

```go
pet := structure {
  name string
  kind string
}{
  name: "Fido",
  kind: "dog",
}
```

Anonymous structs are handy in two common situations. The first is when you translate external data into a structure or a structure into external data
(like JSON or Protocol Buffers). This is called *unmarshaling* and *marshaling* data, respectively.

