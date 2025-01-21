# List and Dictionarl Comprehension

## Creating a list using list comprehension

```python
# The standard way:

numbers = [1, 2, 3, 4, 5]
new_list = []
for number in numbers:
    new_list.append(number + 1)


# Using list comprehension

new_list = [number + 1 for number in numbers]
```

Exercise:

- Create a list using range from 1 to 5 where eacn numes is doubled.

```python
doubled_list = [i * 2 for i in range(1,5)]
# Output: [2, 4, 6, 8]
```

### Conditionals in List Comprehension

 ```python
# The standard way:

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = []
for name in names:
    if len(name) < 5:
        short_names.append(name)

# Using list comprehension

short_names = [name for name in names if len(name) < 5]
# Output: ['Alex', 'Beth', 'Dave']
```

#### Exercise

Create a list from the names, but make all the letters uppercase.

```python
upper_case_names =[name.upper() for name in names if len(name) > 5]
```

#### Course Challenge 1

Square numbers:

```python
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)
```

Even Numbers:

```python
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(s) for s in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)
```

From files:

```python
file1 = ""
file2 = ""

with open("file1.txt") as file:
    file1 = file.read().splitlines()
    

with open("file2.txt") as file:
    file2 = file.read().splitlines()
    

result = [int(str) for str in file1 if str in file2]

print(result)
```

## Dictionary Comprehension

Signature:

```python
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key, value) in dict.items()}
```

```python
# The standard way:

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_dict = {}
for name in names:
    new_dict[name] = len(name)

# Using dictionary comprehension

new_dict = {name: len(name) for name in names}
# Output: {'Alex': 4, 'Beth': 4, 'Caroline': 8, 'Dave': 4, 'Eleanor': 7, 'Freddie': 7}
```

```python
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name: random.randint(1, 100) for name in names}
print(student_scores)

passed_students = {name: score for (name, score) in student_scores.items() if score >= 60}
```

### Course Exercise 2

```python
# letter count
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split(" ")}
print(result)
```

```python
# convert temperatures from Celsius to Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}

print(weather_f)
```
