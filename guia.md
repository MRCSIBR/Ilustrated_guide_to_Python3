# Resumen Python

# VARIABLES AND DATA TYPES

## Variable assignment

```python
name = "John"
age = 25
is_student = True
```

## Data types
```python
string_var = "Hello, World!"
integer_var = 42
float_var = 3.14
boolean_var = True
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3)
dictionary_var = {"name": "John", "age": 25}
```

# CONTROL STRUCTURES

## If-else statement
```python
if age < 18:
    print("You are underage.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

## For loop
```python
for i in range(1, 6):
    print(i)
```

## While loop
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

# FUNCTIONS

## Function definition
```python
def greet(name):
    print("Hello, " + name + "!")
```

## Function call
```python
greet("Alice")
```

# FILE HANDLING

## Read from a file
```python
with open("file.txt", "r") as file:
    contents = file.read()
    print(contents)
```

## Write to a file
```python
with open("file.txt", "w") as file:
    file.write("Hello, World!")
```

# OBJECT-ORIENTED PROGRAMMING

## Class definition
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self age = age

    def greet(self):
        print("Hello, my name is " + self.name + ".")
```

## Object creation and method call
```python
person = Person("John", 25)
person.greet()
```

# ERROR HANDLING

## Try-except block
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
```

# MODULES

## Importing a module
```python
import math
```

## Using functions from a module
```python
print(math.sqrt(16))
```

# BEST PRACTICES

## Commenting
```python
# This is a comment.
```

## Code indentation
```python
def my_function():
    if condition:
        # Do something
    else:
        # Do something else
```

## Naming conventions
```python
variable_name = "value"
function_name = my_function
```

# CLEAN, EFFICIENT, AND MAINTAINABLE CODE

## Avoiding magic numbers
```python
radius = 5
area = math.pi * radius ** 2
```

## Code optimization
```python
result = sum([i for i in range(1, 101)])
```
