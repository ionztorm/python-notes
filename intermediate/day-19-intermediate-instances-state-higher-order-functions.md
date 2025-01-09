# Instances, state, higher order functions

## Instances



## State



## Higher Order Functions

- A higher order function is a function that:
  - Accepts another function as an input
  and/or
  - Returns a function

```py
def add(n1,n2):
    return n1 + n2


def sub(n1,n2):
    return n1 - n2


def mult(n1,n2):
    return n1 * n2


def div(n1,n2):
    return n1 / n2


def calculator(n1,n2,func):
    return func(n1,n2)

add_result = calculator(2,2,add)
```
