# VARIABLES AND DATA TYPES

# Variable assignment
name = "John"
age = 25
is_student = True

# Data types
string_var = "Hello, World!"
integer_var = 42
float_var = 3.14
boolean_var = True
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3)
dictionary_var = {"name": "John", "age": 25}

# CONTROL STRUCTURES

# If-else statement
if age < 18:
    print("You are underage.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# For loop
for i in range(1, 6):
    print(i)

# While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# FUNCTIONS

# Function definition
def greet(name):
    print("Hello, " + name + "!")

# Function call
greet("Alice")

# FILE HANDLING

# Read from a file
with open("file.txt", "r") as file:
    contents = file.read()
    print(contents)

# Write to a file
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# OBJECT-ORIENTED PROGRAMMING

# Class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + ".")

# Object creation and method call
person = Person("John", 25)
person.greet()

# ERROR HANDLING

# Try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# MODULES

# Importing a module
import math

# Using functions from a module
print(math.sqrt(16))

# BEST PRACTICES

# Commenting
# This is a comment.

# Code indentation
def my_function():
    if condition:
        # Do something
    else:
        # Do something else

# Naming conventions
variable_name = "value"
function_name = my_function

# CLEAN, EFFICIENT, AND MAINTAINABLE CODE

# Avoiding magic numbers
radius = 5
area = math.pi * radius ** 2

# Code optimization
result = sum([i for i in range(1, 101)])

# Proper code organization
# Code should be organized into functions, classes, and modules for clarity and reusability.

