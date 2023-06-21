#hello world
print("Hello, World!")

#if else
age =input("your age: ")
if int(age) >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#if elif else and
temperature = input("temperature: ")
temperature=int(temperature)
if temperature < 0:
    print("It's freezing!")
elif temperature >= 0 and temperature <= 25:
    print("It's a pleasant day.")
else:
    print("It's hot outside!")

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

greet(input("What is your name: "))

#Tuples: similar to lists but are immutable
person = ("John", 25, "USA")
print(person)

#dictionary
person = {"name": "John", "age": 25, "country": "USA"}
print(person["name"])  # Output: "John"

# Sets are unordered collections of unique elements.
numbers = {1, 2, 3, 4, 5}

if (input("open file?: ")=='yes'):
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



