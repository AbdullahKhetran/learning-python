# Inheritence: When one class (child) inherits from another (parent)


# The __init__() method for child class
# will initialize any attributes that were defined in the parent class

# Rules
# 1. Parent class must be in the same file
# 2. Parent class should appear above child class
# 3. Parent class name should be in parentheses of child class


# parent class
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formattted descriptive name"""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


# child class
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
