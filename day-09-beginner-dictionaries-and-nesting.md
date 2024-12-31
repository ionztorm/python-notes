# Dictionaries and Nesting

## Dictionaries

### Definition

- Python dictionaries are a collection of key-value pairs.
- We define a dictionary using curly braces `{}`, and the signature is `key: value`.
- We can store a dictionary in a variable.
- Keys are unique within a dictionary, but values can be duplicated.
- A key must be defined as a string, enclosed in quotes, a number, or a tuple.

```python
person = {
    "name": "Leon",
    "age": 41,
    "city": "Liverpool"
}
```

### Accessing Values

- We can access the values in a dictionary using the key.

```python
print(person["name"])
# Output: Leon
```

- We can also use the `get()` method to access the values in a dictionary.

```python
print(person.get("age"))
# Output: 41
```

### Changing Values

- We can also change the value of a key in a dictionary.

```python
person["city"] = "London"
print(person)
# Output: {'name': 'Leon', 'age': 41, 'city': 'London'}
```

### Adding New Key-Value Pairs

- We can add new key-value pairs to a dictionary.

```python
person["country"] = "UK"
print(person)
# Output: {'name': 'Leon', 'age': 41, 'city': 'London', 'country': 'UK'}
```

### Removing Key-Value Pairs

- We can also remove key-value pairs from a dictionary using the `del` keyword.

```python
del person["city"]
print(person)
# Output: {'name': 'Leon', 'age': 41, 'country': 'UK'}
```

### Creating an Empty Dictionary or Wiping a Dictionary

- We can create an empty dictionary, or remove all key-value pairs using curly braces `{}`.

```python
dictionary = {}
```

- We can also remove all key-value pairs from a dictionary using the `clear()` method.

```python
person.clear()
print(person)
# Output: {}
```

### Iterating Over a Dictionary

- We can iterate over a dictionary using a `for` loop.
- By default, the loop will iterate over the keys in the dictionary.

```python
for key in person:
    print(key)
    print(person[key])
# Output:   name    age     country
#           Leon    41      UK
``` 

- We can also iterate over the values in a dictionary.

```python
for value in person.values():
    print(value)
# Output:   Leon    41    UK
```

- We can iterate over both the keys and values in a dictionary using the `items()` method.

```python
for key, value in person.items():
    print(key, value)
# Output:   name Leon    age 41    country UK
```

### KeyError

- If we try to access a key that does not exist in a dictionary, we will get a `KeyError`.

```python
print(person["job"])
# Output: KeyError: 'job'
```

### References and Side Effects

- When we assign a dictionary to a new variable, we are creating a reference to the original dictionary.
- We are not storing the dictionary itself in the new variable.
- This means that when we modify a new variable, the original dictionary is also modified.

```python
person = {
    "name": "Leon",
    "age": 41,
    "city": "Liverpool"
}

new_person = person

new_person["city"] = "London"

print(person)
# Output: {'name': 'Leon', 'age': 41, 'city': 'London'}
```

- This is also true when passing a dictionary as an argument to a function.

```python
def change_city(person):
    person["city"] = "London"

change_city(person)

print(person)
# Output: {'name': 'Leon', 'age': 41, 'city': 'London'}
```

## Nesting

- Lists and dictionaries can be nested inside each other.
- We can create a list of dictionaries, a dictionary of lists, a list of lists, or a dictionary of dictionaries.
- Tuple can also be nested inside a list or dictionary.
- This is called nesting.

```python
# List of Dictionaries
people = [
    {"name": "Leon", "age": 41, "city": "Liverpool"},
    {"name": "Alice", "age": 25, "city": "London"}
    {"name": "Bob", "age": 30, "city": "Manchester"}
]

# Dictionary of Lists
person = {
    "name": ["Leon", "Alice", "Bob"],
    "age": [41, 25, 30],
    "city": ["Liverpool", "London", "Manchester"]
}

# List of Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Dictionary of Dictionaries

people = {
    "Leon": {
        "age": 41,
        "city": "Liverpool"
    },
    "Alice": {
        "age": 25,
        "city": "London"
    },
    "Bob": {
        "age": 30,
        "city": "Manchester"
    }
}
```


