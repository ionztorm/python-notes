# Functions with Parameters and the Caesar Cipher

## Functions with Inputs

- Functions can accept data or even functions as inputs.
- Function inputs are often called **parameters** or **arguments**.
- There is a difference between **parameters** and **arguments**:
  - **Parameters** are used when defining a function - they are the variable or placeholder names that are used in the function definition.
  - **Arguments** are used when calling a function - they are the values that are passed to the function when it is called.
- A function can have multiple parameters and therefore can take multiple arguments - there is no limit on the number of arguments a function can take.
- Parameters are defined within the parentheses `()` in the function definition and are separated by commas.
- Arguments are passed to the function within the parentheses `()` in the function call and are also separated by commas.
- When calling a function, the arguments must be passed in the same order as the parameters in the function definition.
- The number of arguments must match the number of parameters.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

- In the above example, `name` is a parameter of the `greet()` function, and `"Alice"` is an argument passed to the function when it is called.

## Positional vs. Keyword Arguments

- When calling a function, arguments can be passed as **positional arguments** or **keyword arguments**.
- Positional arguments must be passed in the same order as the parameters in the function definition.
- Keyword arguments are passed with the parameter name as a keyword.
- When using keyword arguments, the order of the arguments does not matter.

```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(name="Alice", age=25)
greet(age=25, name="Alice")
```

## Caesar Cipher

- The Caesar cipher is a simple encryption technique that shifts the letters of the alphabet by a fixed number of positions.
- For example, with a shift of 1, `A` would be replaced by `B`, `B` would become `C`, and so on.

