# Day 2 Beginner - Understanding Data Types and String Manipulation

## Contents

- [Primitive Data Types](#primitive-data-types)
- [String Manipulation](#string-manipulation)
  - [Subscripting](#subscripting)
  - [Concatenation](#concatenation)
- [Integers](#integers)
  - [Large Integers](#large-integers)
- [Float (Floating-Point Numbers)](#float-floating-point-numbers)
- [Boolean](#boolean)
- [Type Error](#type-error)
- [Type Checking and Type Conversion](#type-checking-and-type-conversion)
- [Number Manipulation](#number-manipulation)
  - [Mathematically Operations](#mathematically-operations)
  - [Augmented Assignment Operator](#augmented-assignment-operator)
  - [Operation Precedence](#operation-precedence)
  - [Rounding Numbers](#rounding-numbers)
- [f-Strings](#f-strings)




## Primitive Data Types

There are four primitive data types in Python:

- **int** (integer): A whole number.
- **float** (floating-point number): A number with a decimal point.
- **bool** (boolean): A binary value that is either **True** or **False**.
- **str** (string): A sequence of characters enclosed in single or double quotes.

```python
# Examples of primitive data types
print(123)  # int
print(3.14)  # float
print(True)  # bool
print("Hello")  # str
```
## String Manipulation

### Subscripting

- You can access individual characters in a string using subscripting.
- This is done by placing the index of the character in square brackets after the string.
- The index starts at 0 for the first character and increases by 1 for each subsequent character.

```python
word = "Hello"
print(word[0])  # Output: H
print(word[1])  # Output: e
```

- You can also use negative indices to access characters from the end of the string.
- The index -1 refers to the last character, -2 refers to the second last character, and so on.

```python
word = "Hello"
print(word[-1])  # Output: o
print(word[-2])  # Output: l
```

### Concatenation

- You can concatenate (combine) strings using the **+** operator.

```python
greeting = "Hello"
name = "Leon"
message = greeting + " " + name
print(message)  # Output: Hello Leon
```

```python
num1 = "123"
num2 = "456"
result = num1 + num2
print(result)  # Output: 123456
```
## Integers

### Large Integers

- When working with large integers, you can use underscores to make them more readable.
- In the below example, 1_000_000 is equivalent to 1,000,000.
```python
num = 1_000_000
print(num)  # Output: 1000000
```
## Float (Floating-Point Numbers)

- Floating-point numbers are numbers with a decimal point.
- You can perform arithmetic operations on floating-point numbers.

```python
num1 = 3.14
num2 = 1.618
result = num1 + num2
print(result)  # Output: 4.758
```

## Boolean

- Booleans are binary values that are either **True** or **False**.
- You can use comparison operators to get boolean values.
- **True** and **False** are case-sensitive, and must be capitalised.

```python
print(5 > 3)  # Output: True
print(5 < 3)  # Output: False
```
## Type Error

- You will get a **TypeError** if you try to perform an operation on two different data types.
- For example, you cannot add an integer and a string.
- The error message will tell you which data types are involved in the operation.
- The error message in the below example means that the **+** operator does not support adding an integer and a string.

```python
num = 123
name = "Leon"
result = num + name
# Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

- You can convert between data types using type conversion functions.

## Type Checking and Type Conversion

- You can check the data type of a value using the **type** function.

```python
num = 123
print(type(num))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
print(type(True))  # Output: <class 'bool'>
print(type("Hello"))  # Output: <class 'str'>
```
- You can convert between data types using type conversion functions.
- The most common type conversion functions are:
  - **int()**: Converts a value to an integer.
  - **float()**: Converts a value to a floating-point number.
  - **str()**: Converts a value to a string.
  - **bool()**: Converts a value to a boolean.

```python
# Examples of type conversion
num = 123
print(type(num))  # Output: <class 'int'>

num = float(num)
print(type(num))  # Output: <class 'float'>

num = str(num)
print(type(num))  # Output: <class 'str'>

num = bool(num)
print(type(num))  # Output: <class 'bool'>
```

- If you try to convert a data type that is not compatible, you will get a **ValueError**.
- For example, you cannot convert a string that is not a number to an integer.

```python
num = "Hello"
num = int(num)
# Output: ValueError: invalid literal for int() with base 10: 'Hello'
```
## Number Manipulation

### Mathematically Operations

- You can perform mathematical operations on numbers.
- The common mathematical operations are:
  - **+**: Addition
  - **-**: Subtraction
  - **\***: Multiplication
  - **/**: Division - always returns a floating-point number, even if the result is a whole number. This is called implicit type casting.
  - **%**: Modulus (remainder) - returns the remainder of the division operation, e.g., 10 % 3 = 1 because 10 divided by 3 is 3 with a remainder of 1.
  - **\*\***: Exponentiation (power)
  - **//**: Floor division - returns the integer part of the division result - always rounds down.
```python
num1 = 10
num2 = 3
print(num1 + num2)  # Output: 13
print(num1 - num2)  # Output: 7
print(num1 * num2)  # Output: 30
print(num1 / num2)  # Output: 3.3333333333333335
print(num1 % num2)  # Output: 1
print(num1 ** num2)  # Output: 1000
print(num1 // num2)  # Output: 3
```

### Augmented Assignment Operator

- You can increment and decrement a variable using the **+=** and **-=** operators.

```python
num = 10
num += 5
print(num)  # Output: 15

num -= 3
print(num)  # Output: 12
```

### Operation Precedence

- The order of operations in Python is as follows:
  - Parentheses
  - Exponents
  - Multiplication and Division
  - Addition and Subtraction
- Also known as **PEMDAS** (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction).

```python
result = 10 + 3 * 2
print(result)  # Output: 16
```
- Multiple operations of the same precedence level are evaluated from left to right.

- For example, addition and subtraction have the same precedence level, so they are evaluated from left to right.

```python
result = 10 + 3 - 2
print(result)  # Output: 11
```
- Multiplication and division have the same precedence level, so they are evaluated from left to right.

```python
result = 10 * 3 / 2
print(result)  # Output: 15.0
```
- Exponents have the highest precedence level.

```python
result = 10 + 3 ** 2
print(result)  # Output: 19
```

- In the below example, the following operations are performed:
  - 3 * 3 = 9 - Multiplication has a higher precedence than addition so we get 3 * 3 first.
  - 3 / 3 = 1 - Division has a higher precedence than addition so we get 3 / 3 next, before performing the addition.
  - 9 + 1 = 10 - now we perform the addition - we do this befor the subtraction because addition and subtraction have the same precedence level, so we prioritise the operation on the left.
  - 10 - 3 = 7
- The result is 7.0 because the division operation always returns a floating-point number.

```python
print(3 * 3 + 3 / 3 - 3)  # Output: 7.0
```
- However, from the PEMDAS rule, we know that parentheses have the highest precedence level. 
- In the below example, we use parentheses to change the order of operations.
  - (3 + 3) = 6 - we perform the addition first because parentheses have the highest precedence level.
  - 3 * 6 = 18 - now we perform the multiplication.
  - 18 / 3 = 6 - now we perform the division.
  - 6 - 3 = 3 - finally, we perform the subtraction.

```python
print(3 * (3 + 3) / 3 - 3)  # Output: 3.0
```

### Rounding Numbers

- You can round floating-point numbers using the **round** function.
- By default, the **round** function rounds to the nearest whole number.

```python
num = 3.14159
print(round(num))  # Output: 3
```
- You can specify the number of decimal places to round to by passing a second argument to the **round** function.

```python
num = 3.14159
print(round(num, 2))  # Output: 3.14
```

## f-Strings

- f-strings are a way to format strings in Python.
- You can use f-strings to embed expressions inside string literals, using curly braces **{}**.
- The expression inside the curly braces is evaluated and the result is inserted into the string.

```python
name = "Leon"
age = 41
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Leon and I am 41 years old.
```

- If you've studied JavaScript, you can think of f-strings as similar to template literals.

- You can also perform operations inside the curly braces.

```python
num1 = 10
num2 = 3
print(f"{num1} + {num2} = {num1 + num2}")
# Output: 10 + 3 = 13
```

- You can round numbers inside f-strings.
- In the below example, **:.2f** rounds the number to two decimal places.
- This method is called string formatting.
- The :.2f is a format specifier that tells Python to format the number as a floating-point number with two decimal places.

```python
num = 3.14159
print(f"Pi is approximately {num:.2f}")
# Output: Pi is approximately 3.14
```

## Day 2 Project: Tip Calculator

### Instructions

1. Create a greeting for your program.
2. Ask the user for the total bill.
3. Ask the user for the percentage tip they would like to give.
4. Ask the user for the number of people to split the bill.
5. Calculate the total bill with tip and the amount each person should pay.
6. Make sure the input cursor shows on a new line.

```python
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n"))
people = int(input("How many people to split the bill?\n"))
# tip_float = float(str(1) + "." + str(tip)) - bit daft, but it works.
individual_bill = bill * (tip / 100 + 1) / people
# individual_bill = bill * tip_float / people

print(f"Each person needs to pay ${individual_bill:.2f}")
```
