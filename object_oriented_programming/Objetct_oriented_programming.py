class MyClass:
    # Constructor method
    def __init__(self, name):
        self.name = name

    # Instance method
    def say_hello(self):
        print("Hello, " + self.name + "!")

# Create an object of the class
obj = MyClass("Alice")

# Access object's attributes
print(obj.name)

# Call object's methods
obj.say_hello()
