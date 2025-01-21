# Control Flow and Logical Operators

## Comparison Operators

**>** Greater than
**<** Less than
**>=** Greater than or equal to
**<=** Less than or equal to
**==** Equal to
**!=** Not equal to


## Code Flow: if, elif, else

```python
if condition:
  do this
elif condition:
  do this
else:
  do this
```

### Example: BMI Calculator

```python
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / height ** 2

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are under
weight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese
class 1.")
elif bmi < 40:
  print(f"Your BMI is {bmi}, you are obese
class 2.")
else:
  print(f"Your BMI is {bmi}, you
are obese class 3.")
```

## Nested if statements

```python
if condition:
  if another condition:
    do this
  else:
    do this
else:
  do this
```
### Example: Minimum wage salary

```python
age = int(input("How old are you? "))

if age < 18:
  print("Your salary is £5.00 per hour.")
else:
  if age >= 18 and age <= 21:
    print("Your salary is £9.00 per hour.")
  else:
    print("Your salary is £12.00 per hour.")
```

## Example: Odd or Even

```python
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
```

## Python Pizza Exercise

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

```python
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price = 0

# work out how much they need to pay based on their size choice:

if size.lower() == 's':
    price += 15
elif size.lower() == 'm':
    price = +20
elif size.lower() == 'l':
    price = +25
else:
    print(f"Invalid size selected: {size}. Please choose from only 'S', 'M', or 'L'.")

if pepperoni.lower() == 'y':
    if size.lower() == 's':
        price += 2
    else:
        price += 3

if extra_cheese.lower() == 'y':
    price += 1

print(f"Your pizza order comes to £{price:.2f}")
```

## Logical Operators

**and** Both conditions must be true
**or** Either condition must be true
**not** Opposite of the condition

```python
# and

True and True = True
True and False = False

# or

True or True = True
True or False = True
False or False = False

# not

not True = False
not False = True
```


## Day 3 Project: Treasure Island

```python
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = input("You are at a crossroad. Do you want to turn left, or right? (L or R):\n")
if not turn.lower() == 'l':
    print("You fell into a hole.\nGame over.")
else:
    action = input("You arrived at a lake. Do you want to swim or wait? (S or W)\n")

    if not action.lower() == 'w':
        print("You were attacked by trout.\nGame Over.")
    else:
        door = input("You arrive at a set of doors. Which will you choose? [R]ed, [Y]ellow, or [B]lue:\n")

        if door.lower() == 'y':
            print("You found the treasure, You Win!")
        elif door.lower() == 'r':
            print("The room is filled with fire - you died.\nGame Over.")
        elif door.lower() == 'b':
            print("You were eaten by beasts\nGame Over.")
        else:
            print("Game Over")

```
