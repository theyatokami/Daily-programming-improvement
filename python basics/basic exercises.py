#hello world
print("Hello, World!")

#if else
age =input("your age: ")
age=int(age)
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#if elif else and
country = input("Country: ")

if country == "france":
    print("ok")
elif country != "france" and age <= 18:
    print("Go home little kid")
else:
    print("Go home my friend")

#list and for loop
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: "apple"
fruits[1] = "orange"
fruits.append("grape")
for fruit in fruits:
    print(fruit)
#while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

#functions
def greet(name):
    print("Hello, " + name + "!")
name=input("What is your name: ")
greet(name)

#Tuples: similar to lists but are immutable
person = (name, age, country)
print(person)

#dictionary
person = {"name": name, "age": age, "country": country}
print(person["name"])  # Output: "John"

# Sets are unordered collections of unique elements.
numbers = {1, 2, 3, 4, 5}

#files (try except)
if (input("open file?: ")=='yes'):
    try:
        #READ
        file = open("file1.txt", "r")
        content = file.read()
        print(content)
        file.close()
        #OVERWRITE
        file = open("filename.txt", "w")  # Open file in write mode
        file.write("I overwrote this file")
        file.close()
        #ADD
        file = open("filename.txt", "a")  # Open file in append mode
        file.write("this content was appended")
        file.close()
    except FileNotFoundError:
        print("File not found!")
#modules
import modules.my_module1
modules.my_module1.attack(name)

import requests

response = requests.get("https://www.example.com", verify=False)
print(response.text)
