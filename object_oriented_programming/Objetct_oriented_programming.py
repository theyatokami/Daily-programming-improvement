class MyClass:
    # Constructor method
    def __init__(self, name):
        self.name = name

    # Instance method
    def say_hello(self):
        print("Hello, " + self.name + "!")

# Create an object of the class
obj = MyClass("User")

# Access object's attributes
print(obj.name)

# Call object's methods
obj.say_hello()

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("An animal speaks.")

# Derived class
class Dog(Animal):
    def speak(self):
        print("Dog barks.")

# Create objects of the classes
animal = Animal("Generic Animal")
dog = Dog("Bobby")

# Call methods
animal.speak()
dog.speak()
