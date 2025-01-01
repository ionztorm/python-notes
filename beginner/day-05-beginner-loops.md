# Python Loops

## The For Loop

```python
for item in list_of_items:
    do something to each item
```

- For example:

```python
fruits = ["apple", "banana", "pear"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# pear
```

### For .. in range ..

- We can also use the `for... in range ..` loop:

```python
for item in range(a,b):
    do something to each item
```

- The `range` keyword accepts 3 arguments:

  1. The start - optional with a default of 0. Specifies at which position to start.
  2. The end - required. Specifies at which point to end.
  3. The step - optional with a default of 1. Specifies the increment at which item increases.

- Note that the `end` is not inclusive. Similar to accessing list indexes, the end specifies which number to stop before.

```python
for i in range(6):
    print(i)
# prints numbers 0 - 5

for i in range(3,20):
    print(i)
# prints numbers 3 - 19

for i in range(2,20,2):
    print(i)
# prints 2, 4, 6, 8, 10, 12, 14, 16, 18
```

## Day 5: Password Generator

Create a password generator that accepts user input for a number of letters, symbols, and numbers.

```python
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(0, nr_letters):
    password.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    password.append(random.choice(symbols))

for number in range(0, nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
final_password = "".join(password)

print(final_password)
```
