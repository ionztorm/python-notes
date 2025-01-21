# Functions with Outputs and Doc Strings

## Functions with Outputs

### The return Statement

- Functions can also be used to return values.
- **Return** is a keyword that allows you to send data back from the function call to the line of code that called the function.

```python
def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

formatted_full_name = format_name("leon", "lonsdale")
```
### Multiple Return Values

- The return statement signals the end of a function and sends data back to the caller.
- Any functionality that is written after the return statement, and within the same block, is not executed.
- It can therefore be used as an **early return** or exit from a function.

```python
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"{f_name.title()} {l_name.title()}"
```

### Leap Year Exercise:

```python
def is_leap_year(year):
    
    if (year % 100 == 0 and not year % 400 == 0) or not year % 4 == 0:
        return False
    
    return True
```

## Doc Strings

- Doc Strings are used to document the purpose of a function.
- The information documented in a Doc String is displayed when the by text editors and IDEs when the function is hovered.
- The DocString must be the first line after the function definition.
- The syntax for a Doc String is three double quotes `"""` followed by the description of the function.

```python
def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"{f_name.title()} {l_name.title()}"
```
