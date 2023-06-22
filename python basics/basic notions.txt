my_string = "Hello, World!"
my_integer = 10
my_float = 10.5
my_boolean = True
my_list = [1, 2, 3, "a", "b", "c"]
my_dict = {"key1": "value1", "key2": "value2"}
#Python has several types of operators:
#Arithmetic operators: +, -, *, /, // (integer division), ** (exponentiation), % (modulus)
#Comparison operators: == (equal to), != (not equal to), >, <, >=, <=
#Logical operators: and, or, not
# Assignment operators: =, +=, -=, *=, /=, etc.

for i in range(10):
    print(i)

# Define a list
fruits = ["apple", "banana", "cherry"]
# Add an item to the end of the list
fruits.append("dragonfruit")
# Remove an item from the list
fruits.remove("banana")
# Change an item in the list
fruits[0] = "avocado"

# List comprehension (create a new list based on the old one)
new_list = [fruit.upper() for fruit in fruits]  # Creates a new list with all the fruit names in uppercase
# Define a dictionary
person = {"name": "Alice", "age": 25}
# Access a value
print(person["name"])  # Outputs: Alice
# Change a value
person["age"] = 26
# Add a new key-value pair
person["profession"] = "Engineer"
# Remove a key-value pair
del person["age"]

try:
    # Code that might cause an error
    x = 1 / 0
except ZeroDivisionError:
    # Code to run if that error happens
    print("You can't divide by zero!")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old")
# Create an object of type Person
alice = Person("Alice", 25)
# Call the object's method
alice.greet()

# Import the entire math library
import math
print(math.sqrt(16))  # Outputs: 4.0
# Import only the sqrt function from the math library
from math import sqrt
print(sqrt(16))  # Outputs: 4.0
# Import the math library under a different name
import math as m
print(m.sqrt(16))  # Outputs: 4.0

# Writing to a file
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
# Reading from a file
with open('file.txt', 'r') as f:
    print(f.read())

import re
# Search for a pattern in a string
if re.search('world', 'Hello, world!'):
    print('Match found')
else:
    print('No match')

# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))  # Outputs: 15

numbers = [1, 2, 3, 4, 5]
# Using map function
squared = list(map(lambda x: x**2, numbers))  # Outputs: [1, 4, 9, 16, 25]
# Using filter function
evens = list(filter(lambda x: x%2 == 0, numbers))  # Outputs: [2, 4]
# Using reduce function
from functools import reduce
product = reduce((lambda x, y: x * y), numbers)  # Outputs: 120

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get all elements from index 2 to 5
print(numbers[2:6])  # Outputs: [2, 3, 4, 5]
# Get all elements from the start to index 3
print(numbers[:4])  # Outputs: [0, 1, 2, 3]
# Get all elements from index 4 to the end
print(numbers[4:])  # Outputs: [4, 5, 6, 7, 8, 9]
# Get every other element of the list
print(numbers[::2])  # Outputs: [0, 2, 4, 6, 8]
# Reverse the list
print(numbers[::-1])  # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
