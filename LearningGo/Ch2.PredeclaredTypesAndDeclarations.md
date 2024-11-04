# Chapter 2. Predeclared Types and Declarations 

## The Predeclared Types

### The Zero Value

Go assigns a default *zero* value to any variable that is declared but not assigned a value.

### Literals

A Go *literal* is an explicitly specified number, character, or string.  
Go programs have four common kinds of literals.

1. An *integer literal* is a sequence of numbers. Integer literals are base 10 by default. To make it easier to read longer integer literals, Go allows you to put underscores in the middle of your literal. For example, 1_234.
2. A *floating-point literal* has a decimal point to indicate the fractional portion of the value. For example, 6.03e23.
3. A *rune literal* represents a chracter and is surrounded by single quotes. Unlike many other languages, in Go single quotes and double quotes are *not* interchangeable.
4. There are tow ways to indicate *string literals*. Most of the time, you should use double quotes to create and *interpreted string literal*(e.g., type "Greetings and Salutations"). These contain zero or more rune literals.
   They are called "interpreted" because they interpret rune literals into single chracters.

### Booleans

The zero value for a bool is false

### Numeric Types

Go has a large number of numeric types: 12 types.

You should follow three simple rules to choose which integer to use:

1. If you are working with a binary file format or network protocol that has an integer of a specific size or sign, use the corresponding integer type.
2. If you are writing a library fuction that should work with any integer type, take advantage of Go's generics support and use a generic type parameter to represent any integer type
3. In all other cases, just use int.

## var Versus :=

### Use var

`var x int = 10`

If the ype on the righthand of the `=` is the expected type of your variable, you can leave off the type from the left side of the `=`. 
Since the default type of an integer literal is int, the following declares x to be a variable of type int:

`var x = 10`

Conversely, if you want to declare a varaible and assign it the zero value, you can keep the type and drop the `=` on the righthand side:

`var x int`

You can declare multiple variables at once with var, and they can be of the same type,

`var x, y int = 10, 20`

or of different types:

`var x, y = 10, "hello"`

There's one more ways to use `var`. If you are declaring multiple variables at once, you can wrap them in a *declaration list*:

```go
var (
  x  int
  y    = 20
  z int = 30
  d,e = 40, "hello"
  f,g string
)
```

When you are within a function, you can use the `:=` operator to replace a `var` declaration that uses type inference.
The following tow statements do exactly the same thing

```go
var x = 10
x := 10
```

```go
var x,y = 10, "hello"
x,y := 10, "hello"
```

The `:=` operator can do on trick that you cannot do with `var`. it allows you to assign values to existing variables too.

```go
x := 10
x,y := 30, "hello"
```

Using `:=` has on limitation. If you are declaring a variable at the package level, you must use `var` because `:=` is no legal outside of functions.

The most common declaration style within function is `:=`. Outside of a function, use declaration lists on the rare occasions when you are declaring multiple package-level variables.
However, You should rarely declare variables outside of functions, in what's called the package block. Package-level variables whose values change are a bad idea. 
When you have a variable outside of a function, it can be difficult to track the changes made to it, which makes it hard to understand how data is flowing through your program.

## Using const

Using `const` declare a value as immutable.

Go doesn't provide a way to specify that a value calculated at runtime is immutable. For example, the following code will fail to compile with the error x + y (value of type int) is not constant:

```go
x := 5
y := 10
const z = x + y // this won't compile!
```

There are no immutable arrays, slices, maps, or structs, and there's no way to declare that a field in a structure is immutable.

## Unused Variables

Go requirement is that *every declared local variable must be read*. It is a *compile-time error* to declare a local variable and to not read its value.

## Naming Varaibles and Constants

Idiomatic Go uses camel case.  
In many languages, constants are always written in all uppercase letters, with words separated by underscores. Go doesn't follow this pattern.
This is because Go uses the case of the first letter in the name of a package-level declaration to determine if the item is accessible outside the package.

