# Object Oriented Programming - OOP

## Intro to OOP

OOP involves creating a model of real-world entities.

These models, knwn as `classes`, should define what the entity has and what it does.

- We define what it has using `attributes`. Attributes are variables that store data.
- We define what it does using `methods`. Methots are functions attached to the object that perform actions.

A `class` is a blueprint of the entity, and we can create as many instances of these classes as we need.

The instances we create from the classes are known as `objects`.

Examples of something we might use a class to describe in the workplace are:

- Owner
    - Attributes
        - Name
        - Age
        - Salary
    - Methods
        - Increase Salary
        - Decrease Salary
        - Hire Employee
- Manager
    - Attributes
        - Name
        - Age
        - Salary
    - Methods
        - Increase Salary
        - Decrease Salary
        - Train Employee 
- Employee
    - Attributes
        - Name
        - Age
        - Salary
    - Methods
        - Attend Training
        - Take Break
        - Work
- Cleaner
    - Attributes
        - Name
        - Age
        - Salary
    - Methods
        - Brush
        - Mop
        - Take Break

## Constructing Objects

To create an object from a class we use the following syntax:

```py
object_name = ClassName()
```

## Accessing Attributes

```py
object_name.attribute
```

## Accessing Methods

```py
object_name.method()
```
