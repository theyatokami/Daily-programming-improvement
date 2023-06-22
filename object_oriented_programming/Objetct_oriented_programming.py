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

class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number  # Private attribute

    def get_account_number(self):
        return self.__account_number  # Public method to access private attribute

# Create an object
account = BankAccount("1234567890")

# Access attribute through a public method
print(account.get_account_number())

# Base class
class Shape:
    def calculate_area(self):
        pass  # Abstract method

# Derived classes
class Rectangle(Shape):
    def calculate_area(self, length, width):
        return length * width

class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius * radius

# Create objects and call methods
rectangle = Rectangle()
circle = Circle()

print(rectangle.calculate_area(4, 5))
print(circle.calculate_area(3))

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    
say_hello()
