# Classes

- A Class is a blueprint for creating objects. Objects have properties and methods associated with them. Almost everything in Python is an object, with its properties and methods.
- We name classes using PascalCase, starting with a capital letter.

## Creating a Class

- We use the `class` keyword to define a class.

```py
class User:
    pass
```

**Note**: The `pass` keyword is used when we have a codeblock with no content. It is used to avoid getting an error.

- We can now create an instance of this class, in the form of an object, using this syntax:

```py
user_1 = User()
```

## Adding Attributes

- Thes simplest way (but not tho optimal way) to add attributes to a class is to do so directly on the object.

```py
user_1.first_name = "Dave"
```

- However, this is not very scalable it you have to create many objects with many attributes.

### The __init__ Constructor Method

- The preferred way is to add attributes to the class itself. We do this using a constructor method called `__init__`.
- The constructor allows us to specify what should happen at object is `initialisation`

```py
- This method is called at the moment of creating an object, and initialises the object's state by accepting arguments and assigning them to the object's properties.

```py
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
```

- With the inclusion of the constructor, we can now pass the arguments to the class when instantiating an object.

```py
user_2 = User("John", "Doe", 30)
```

- The `self` keyword is used to refer to the current instance of the class, and is used to access variables that belong to the class. This means when a method utilises `self` it means to look within itself (the object) for the attribute or method being called for using dot notation.
- The constructor/__init__ function always receives `self` as the first parameter, and then any other parameters we want to pass to the class.
- When the `user_2` object is instantiated, the constructor takes `John` and applies it to `self.first_name`, `Doe` and applies it to `self.last_name`, and `30` and applies it to `self.age`.

- However, not all attributes should be passed in, so we can set a default value:


```py
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.followers = 0
```

- We may also want to generate attributes on instantiation:


```py
import uuid

class User:
    def __init__(self, first_name, last_name, age):
        self.user_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.followers = 0
```

## Adding Methods

- Adding methods is as simple as defining a function within the class block.

```py
import uuid

class User:
    def __init__(self, first_name, last_name, age):
        self.user_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.followers = 0

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
```


