# References

## Terminologies

- **Syntax**: The rules that define how code should be written in a programming language.
- **Variable**: A container for storing data values.
- **Data Type**: The classification of data into different categories, such as integers, strings, and booleans.
- **String**: A sequence of characters enclosed in single or double quotes.
- **Integer**: A whole number.
- **Float**: A number with a decimal point.
- **Boolean**: A binary value that is either **True** or **False**.
- **Implicit Type Casting**: The automatic conversion of data from one type to another.
- **Explicit Type Casting**: The manual conversion of data from one type to another.
- **F-String**: A formatted string literal that allows you to embed expressions inside string literals, using curly braces **{}**.
- **Subscripting**: The process of accessing individual characters in a string using their index.
- **Concatenation**: The process of combining strings together.
- **String Formatting**: The process of creating formatted strings using placeholders such as **{}**. Used in F-strings and the **format()** method.


## Useful Functions

- **print()**: A function that prints the specified message to the screen. Signature: **print(value)**.
- **input()**: A function that takes user input and returns it as a string. Signature: **input(prompt)**.
- **len()**: A function that returns the length of a string. Signature: **len(string)**.
- **str()**: A function that converts a value to a string. Signature: **str(value)**. 
- **int()**: A function that converts a value to an integer. Signature: **int(value)**.
- **float()**: A function that converts a value to a float. Signature: **float(value)**.
- **bool()**: A function that converts a value to a boolean. Any non-zero value is considered **True**, while zero is considered **False**. Signature: **bool(value)**.
- **round()**: A function that rounds a number to a specified number of decimal places. Signature: **round(number, ndigits)**.
- **format()**: A method that formats a string using placeholders. Signature: **string.format(value1, value2, ...)**.
- **type()**: A function that returns the data type of a value. Signature: **type(value)**.


## Errors

**TypeError**: Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.

- Introduced in [Day 2](day-02-beginner-understanding-data-types-and-string-manipulation.md)

```python 
num = 123
name = "Leon"
result = num + name
# Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
**ValueError**: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.

- Introduced in [Day 2](day-02-beginner-understanding-data-types-and-string-manipulation.md)

```python
num = "Hello"
num = int(num)
# Output: ValueError: invalid literal for int() with base 10: 'Hello'
```

## Mathematical Operations

- Introduced in [Day 2](day-02-beginner-understanding-data-types-and-string-manipulation.md)

- **Addition**: The **+** operator is used to add two numbers.
- **Subtraction**: The **-** operator is used to subtract one number from another.
- **Multiplication**: The **\*** operator is used to multiply two numbers.
- **Division**: The **/** operator is used to divide one number by another.
- **Exponentiation**: The **\*\*** operator is used to raise a number to the power of another number.
- **Modulus**: The **%** operator is used to find the remainder of the division of two numbers.
- **Floor Division**: The **//** operator is used to find the quotient of the division of two numbers, rounded down to the nearest whole number.
- **Round**: The **round()** function is used to round a number to a specified number of decimal places. It can take two arguments: the number to be rounded and the number of decimal places.


