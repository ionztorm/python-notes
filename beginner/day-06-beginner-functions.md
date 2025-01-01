# Functions and While Loops

## Functions

### Defining and Calling Functions

- Functions are defined using the `def` keyword.
- The syntax for defining a function is `def function_name():`.

```python
def greet():
```
- The code block (more on code blocks later) that makes up the function is indented.
- In Python, the standard is to use 4 spaces for indentation.
- The code block is the code that runs when the function is called.
- The code block can contain any number of lines of code.

```python
def greet():
    print("Hello")
```

### Calling Functions

- Functions are `called` using the function name followed by parentheses.

```python
greet()
# Output: Hello
```

### Function Parameters

- Functions can take parameters.
- A parameter is a value that the function expects you to pass when you call it.
- Parameters are defined inside the parentheses of the function definition.
- When calling a function with parameters, you pass the values inside the parentheses.

```python
def greet(name):
    print(f"Hello {name}")

greet("Leon")
# Output: Hello Leon
```

### Reeborg's World Challenge

[Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Hurdle%201&url=worlds/tutorial_en/hurdle1.json)
```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_and_turn_right():
    move()
    turn_right()
  
def move_and_turn_left():
    move()
    turn_left()
    
def jump_hurdle():
    move_and_turn_left()
    move_and_turn_right()
    move_and_turn_right()
    move_and_turn_left()
 
for i in range(6):
    jump_hurdle()
```
## Code Blocks and Indentation

- Code blocks are an important concept in programming.
- A code block is a group of statements that are treated as a single unit.
- In Python, code blocks are defined by indentation.
- All statements at the same level of indentation are part of the same code block.
- Indentation is used to define the structure of the code.

```python
def greet(name):
    print(f"Hello {name}")
    print("How are you?")
```

- In this example, the two `print` statements are part of the same code block because they have the same level of indentation.
- Code blocks are used in functions, loops, conditionals, and other structures in Python.

```python
# loop code block
for i in range(5):
    print(i)
    print(i * 2)

# conditional code block
if x > 0:
    print("Positive")
    print("Number")
```

## While Loop

- A `while` loop is used to repeat a block of code as long as a condition is `True`.
- The syntax for a `while` loop is `while condition:`.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Reeborg's World Challenge

**Randomly Positioned Hurdles**

[Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Hurdle%203&url=worlds/tutorial_en/hurdle3.json)

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if not front_is_clear():
        jump()
    else:
        move()
```

**Randomly Sized Hurdles**

[Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Hurdle%203&url=worlds/tutorial_en/hurdle3.json)

```python
def turn_right():
    for _ in range(3): turn_left()  
while not at_goal():
    if front_is_clear(): move()
    if right_is_clear(): turn_right()
    if wall_in_front(): turn_left()
```
 
## Day 6 Project: Escaping the Maze

[Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Maze&url=worlds/tutorial_en/maze1.json)

 ```python
def turn_right():
    for _ in range(3): turn_left()
        

while not at_goal():
    
    if front_is_clear() and wall_on_right():
        move()
    elif not wall_on_right():
        turn_right()
        move()
    else:
        turn_left()
```
