# datetime

The `datetime` module supplies classes for manipulating dates and times. 

It comes built-in with Python, so you don't have to install it separately.

## Current Date and Time

One common use of the `datetime` module is getting the current date and time. Here's how you can do that:

```python
import datetime as dt

now = dt.datetime.now()
```

The result will be a `datetime` object representing the current date and time.

This object exposes several methods and attributes that allow you to manipulate dates and times. For example, you can get the current year, month, day, hour, minute, and second like this:

```python
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second  
```

Another often useful method is `weekday`. This method returns the day of the week as an integer, where Monday is 0 and Sunday is 6:

```python
day_of_week = now.weekday()

# 0 = Monday, 1 = Tuesday, 3 = Wednesday, 4 = Thursday
# 5 = Friday, 6 = Saturday, 7 = Sunday
```

## Creating a `datetime` Object

When creating a `datetime` object, you can specify the year, month, day, hour, minute, second, and microsecond. However, the hour, minute, second, and microsecond are optional and default to 0.

Here's an example:

```python
date_of_birth = dt.datetime(1990, 1, 1)
# creates a datetime object representing January 1, 1990
```
