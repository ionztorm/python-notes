# Errors

Errors occur when the program is unable to execute a statement. There are two types of errors

- Syntax errors
- Exceptions

## Syntax errors

A syntax error occurs when the parser detects a statement that does not conform to the grammar of the language. For example, the following code will raise a syntax error.

```python
if True
    print("Missing colon at the end of the if statement")
```

## Exceptions

An exception is an error that occurs during the execution of a program. When an exception occurs, the program stops executing and an error message is displayed. For example, the following code will raise an exception.

```python
numerator = 10
denominator = 0
result = numerator / denominator  # This will raise a ZeroDivisionError
```

## Handling exceptions

We can handle exceptions using the `try` and `except` blocks. The code that might raise an exception is placed inside the `try` block. If an exception occurs, the code inside the `except` block is executed. For example, the following code will handle the `ZeroDivisionError`.

```python
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    print("Division by zero is not allowed")
```

We can add additional keywords: `else` and `finally` to the `try` and `except` blocks.

For example, the following code will handle the `ZeroDivisionError` and print the result if no exception occurs.

```python
try:
    numerator = 10
    denominator = 2
    result = numerator / denominator
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Result:", result)
finally:
    print("Execution completed")
```

The `else` block is executed if no exception occurs. It is typically used to perform additional operations that depend on the successful execution of the `try` block.

The `finally` block is always executed, regardless of whether an exception occurs or not. It is typically used to release resources that were acquired in the `try` block (cleanup).

## Handling multiple exceptions types

```python
file = None
try:
    file = open("a_non_existant_file.txt")
except FileNotFoundError:
    file = open("a_non_existant_file.txt", "w")
except PermissionError:
    print("Permission denied")
except KeyError as message:
    print("Key error:", message)
except Exception as e:
    print("An error occurred:", e)
else:
    print("File opened successfully")
finally:
    file.close()
```

## Raising exceptions

We can raise exceptions using the `raise` statement. 


```python
height = float(input("Enter your height in meters: "))
weight = int(input("Enter your weight in kilograms: "))

if 0 > height > 3:
    raise ValueError("This looks like an invalid height")

bmi = weight / height ** 2

print("Your BMI is:", bmi)
```
