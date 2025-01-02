# Scope

- Scope is the context in which a variable is defined.
- For example, was the variable defined inside a code block, or was it defined at the file level?

## Namespaces: Local vs Global Scope

### Local Scope

- Any entity (variable, function, class, etc.) defined within a block of code is said to have a local scope - meaning it is only accessible within that block of code.

- Local scoped entities exist only during execution of the block of code in which they are defined.
- They do not interfere with entities of the same name defined outside the block of code.

Example:

```python
def outer_function():
    x = 10

    def inner_function():
        y = 20
        x = 30
        print(y) # 20

    inner_function()
    print(x) # 10
    print(y) # NameError: name 'y' is not defined

inner_function()  # NameError: name 'inner_function' is not defined
print(x)  # NameError: name 'x' is not defined
```

### Global Scope

- Any entity defined outside all blocks, at the top level of a file / module is said to have a global scope - meaning it is accessible from anywhere in the code.

- Global scoped entities exist throughout the execution of the program.

- They can be accessed from within any block of code, including functions and classes, but to not interfere with local scoped entities of the same name.

- To modify a global variable from within a function, you must use the `global` keyword.
```python
y = 10

def outer_function():
    x = 20
    print(y)  # 10

    def inner_function():
        print(x)  # 20
        print(y)  # 10
        

    global y = 30

print(y)  # 30
```
- Entities in global scope include:

  - Variables defined at the top level of a module.
  - Functions defined at the top level of a module.
  - Classes defined at the top level of a module.
  - Constants declared at the top level of a module.
  - Imported modules.

### Namespaces

- A namespace is essentially a container that holds a mapping between names (the identifiers) and objects (the values - these are the variables, functions, etc).

- There are a few types of namespaces in Python:
    - Built-in namespace: Contains all the built-in functions and exceptions.
    - Global namespace: Contains all the names defined at the top level of a module.
    - Local namespace: Contains all the names defined within a function.

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # local scope

    inner()
    print(x)  # enclosing scope

outer()
print(x)  # global scope
```

## Block Scope

- There is no such thing as block scope in Python.
- Entities defined within a block of code (e.g. an `if` statement, `for` loop, etc) are still considered to have local scope to the function in which they are defined.

```python
global_var = 10
list_of_cars = ["Ford", "Toyota", "Chevrolet"]

if global_var > 5:
    car = "Ford"

print(car)  # Ford
```

## Modify Global Variables

- To modify a global variable from within a function, you must use the `global` keyword.

```python
x = 10
def modify_global():
    global x
    x = 20

print(x)  # 10
```

### Constants 

- Constants are variables whose values should not change throughout the program.
- The naming convention for constants in Python is to use all uppercase letters with underscores separating words.


```python

