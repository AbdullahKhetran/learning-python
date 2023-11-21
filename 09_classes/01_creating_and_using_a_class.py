# When you write a class, you define the
# general behavior that a whole category of objects can have.

# Making an object from a class is called "instantiation"

# 1
class Dog:
    """A simple attempt to model a dog."""

# 2
    def __init__(self, name, age):
        """Initialize name and age attributes."""
# 3
        self.name = name
        self.age = age

# 4
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# 1 Define a class.
#   capitalized names refer to classes
#   then write docst5ring

# 2 __init__ method
#   2 leading and 2 trailing underscores _
#   python runs this method automatically when a new instance of the
#   class is created
#   self parameter is required and shoud come first. It is passed
#   automatically as an argument when method is called. It gives
#   individual instance access to attributes and methods in the class
#
# 3 self prefix
#   variables prefixed with "self" are available to every method in the
#   class. They can also be access while creating instance
#   `self.name = name` takes the value associated with parameter `name`
#   and assigns it to varibale name and then attach it to the instance
#   variables that are accessible through instance like this are called
#   "attributes"
#
# 4 2 methods
#   they dont need much information so only requried argument 'self' is
#   passed


# Making an instance from a class

my_dog = Dog("Willie", 6)  # 1

print(f"My dog's name is {my_dog.name}")  # 2
print(f"My dog is {my_dog.age} years old")  # 3

# 1
#   we are asking python to create an isntance of Dog class
#   the arguments are also passed
#   python then calls the __init__() method and returns the instance
#   returned instance is stored in `my_dog` variable

# 2 and 3
#   dot notation is used to access the attribute of the isntance

# Calling methods
my_dog.roll_over()
my_dog.sit()


# Creating multiple instances

your_dog = Dog("Lucy", 3)

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
