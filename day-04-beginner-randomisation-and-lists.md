# Randomness

Python uses the Mersenne Twister as the core generator. It produces 53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.

In Python, the `random` module provides a suite of functions for generating random numbers.

[Useful Video](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)

## Modules

- Modules are like toolkits that contain a set of tools (functions) that you can use.
- We can import modules in Python using the `import` keyword.

```python
import random
```

- We can also import specific functions from a module.

```python
from random import randint
```

- We can also give an alias to a module or a function.

```python
import random as r
from random import randint as ri
```

- Modules can be used to organise code and make it more readable.

## Random Module

- Python has a built-in module that you can use to make random numbers.

- The `random` module has a set of methods:

  - `random()`: Returns a random float number between 0 and 1.

  - `randint()`: Returns a random integer number between the specified integers.

  - `choice()`: Returns a random element from the given sequence.

  - `shuffle()`: Takes a sequence and returns the sequence in a random order.

  - `uniform()`: Returns a random float number between two specified numbers.

```python
import random

random_integer = random.randint(1, 10)
print(random_integer)

# We multiply the random float by 5 to get a number between 0.0 and 4.999999999999999
random_float = random.random() * 5
print(random_float)

# We can use the uniform method to get a number between 0.0 and 5.0
random_float = random.uniform(0.0, 5.0)
print(random_float)

# We can use the choice method to get a random element from a list
names = ["Jack", "Jill", "John", "Jane"]
random_name = random.choice(names)
print(random_name)

# We can use the shuffle method to shuffle a list
random.shuffle(names)
print(names)
```

## Heads or Tails

You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".  

**Important**, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

e.g.

1 means Heads

0 means Tails

```python
import random

random_number = random.randint(0, 1)

if random_number == 1:
    print("Heads")
else:
    print("Tails")
```

We could aos use the `choice` method to get a random element from a list.

```python
import random

coin = ["Heads", "Tails"]
print(random.choice(coin))
```

## Lists

- A list is a collection of items in a particular order.
- Lists can contain any data type, and they can contain as many items as we want.
- We can define a list by using square brackets `[]`.
- Items inside the list are separated by commas `,`.
- A list can be assigned to a variable.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits)
```

### Accessing Items

- We can access items in a list by referring to the index number.
- The index number starts from 0.
- The syntax for accessing an item in a list is `list_name[index]`.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[1])
# Output: Banana
```

### Negative Indexing

- Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item, and so on.
- Negative indexing can be useful when you want to access the last item without knowing the length of the list.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[-1])
# Output: Cherry
```

### Range of Indexes

- You can specify a range of indexes by specifying where to start and where to end the range.
- When specifying a range, the return value will be a new list with the specified items.

```python
fruits = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango"]
print(fruits[2:5])
# Output: ['Cherry', 'Orange', 'Kiwi']
```
- This will return the items from index 2 to 4 - it basically means items from index 2 upto, but not including, index 5.

Some more examples:

```python
# This will return the items from index 1 to 4 - [:4] is the same as [1:4]
print(fruits[:4]) # Output: ['Apple', 'Banana', 'Cherry', 'Orange']

# This will return the items from index 2 to the end of the list
print(fruits[2:]) # Output: ['Cherry', 'Orange', 'Kiwi', 'Melon', 'Mango']

# This will return the last item in the list
print(fruits[-1:]) # Output: ['Mango']

# This will return the last two items in the list
print(fruits[-2:]) # Output: ['Melon', 'Mango']
```

We can also add a third parameter to specify the step value.

```python
# This will return every second item in the list
print(fruits[::2]) # Output: ['Apple', 'Cherry', 'Kiwi', 'Mango']
```

### Changing Items

- To change the value of a specific item, refer to the index number and assign a new value.

```python
fruits = ["Apple", "Banana", "Cherry"]
fruits[1] = "Blackcurrant"
print(fruits)
# Output: ['Apple', 'Blackcurrant', 'Cherry']
```

### Adding Items

- To add an item to the end of the list, use the `append()` method.

```python
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Orange")
print(fruits)
# Output: ['Apple', 'Banana', 'Cherry', 'Orange']
```

- To add an item at the specified index, use the `insert()` method.

```python
fruits = ["Apple", "Banana", "Cherry"]
fruits.insert(1, "Orange")
print(fruits)
# Output: ['Apple', 'Orange', 'Banana', 'Cherry']
```

### Extending Lists

- To add all the items from another list to the current list, use the `extend()` method.

```python
fruits = ["Apple", "Banana", "Cherry"]
more_fruits = ["Orange", "Mango", "Grapes"]
fruits.extend(more_fruits)
print(fruits)
# Output: ['Apple', 'Banana', 'Cherry', 'Orange', 'Mango', 'Grapes']
```

### Removing Items

- To remove an item from the list, use the `remove()` method.

```python
fruits = ["Apple", "Banana", "Cherry"]
fruits.remove("Banana")
print(fruits)
# Output: ['Apple', 'Cherry']
```

- To remove an item at the specified index, use the `pop()` method.

```python
fruits = ["Apple", "Banana", "Cherry"]
fruits.pop(1)
print(fruits)
# Output: ['Apple', 'Cherry']
```

- If you do not specify the index, the `pop()` method removes the last item.
- The `pop()` method returns the removed item, so you can store it in a variable.

```python
fruits = ["Apple", "Banana", "Cherry"]
removed_item = fruits.pop()
print(fruits)
# Output: ['Apple', 'Banana']
```

- To remove an item at the specified index, use the `del` keyword.

```python
fruits = ["Apple", "Banana", "Cherry"]
del fruits[1]
print(fruits)
# Output: ['Apple', 'Cherry']
```

- To remove all the items from the list, use the `clear()` method.

```python
fruits = ["Apple", "Banana", "Cherry"]
fruits.clear()
print(fruits)
# Output: []
```

### Challenge Exercise

Select a random name from the list of names.

```python
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Approach 1

import random

random_name = random.choice(names)
print(random_name)


# Approach 2

random_index = random.randint(0, len(names) - 1)
print(names[random_index])
```

## Index Errors

- If you try to access an index that does not exist, you will get an `IndexError`.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[3])
# Output: IndexError: list index out of range
```

- If you try to access an index using a negative number that is too large, you will get an `IndexError`.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[-4])
# Output: IndexError: list index out of range
```

- There is also the out by one error, where you try to access an index that is one more than the last index.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[len(fruits)])
# Output: IndexError: list index out of range
```

- To avoid these errors, you can use the `len()` function to get the length of the list.

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[len(fruits) - 1])
# Output: Cherry
```

## Nested Lists

- A list can contain any data type, including another list.

```python
fruits = ["Apple", "Banana", "Cherry"]
vegetables = ["Carrot", "Potato", "Spinach"]
food = [fruits, vegetables]
print(food)
# Output: [['Apple', 'Banana', 'Cherry'], ['Carrot', 'Potato', 'Spinach']]
```

- To access items in a nested list, use multiple indexes.

```python
print(food[1][0])
# Output: Carrot
```

## Day 4 Project: Rock Paper Scissors

You are going to write a classic rock paper scissors game against the computer.

The rock beats scissors, scissors beat paper, and paper beats rock.

```python
import random

options = ["rock","paper","scissors"]

user_input = input("Make your choice; [1] Rock, [2] Paper, or [3] Scissors: \n")

user_choice = options[int(user_input) - 1]
computer_choice = random.choice(options)

outcome = ""

if (user_choice == "rock" and computer_choice == 'scissors') 
    or (user_choice == 'scissors' and computer_choice == 'paper') 
    or (user_choice == 'paper' and computer_choice == 'rock'):
    outcome = "You win"
elif user_choice == computer_choice:
    outcome = 'It\'s a draw'
else:
    outcome = 'You lose'

print(f"You chose {user_choice}, the computer chose {computer_choice}\n{outcome}")
```
