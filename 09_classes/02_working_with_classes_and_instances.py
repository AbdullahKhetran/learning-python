class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formattted descriptive name"""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())


# Setting a default value for an attribute

# attributes can be defined without being passed in as parameter

class Car_2:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        # attribute that isn't passed as parameter
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formattted descriptive name"""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_car = Car_2("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_car.read_odometer()


# Modifying Attribute Values
# value can be modified in 3 ways:
# 1. Directly
# 2. Through a method
# 3. Incrementing through a method

# 1. Modifying directly
my_car.odometer_reading = 23
my_car.read_odometer()


# 2. Through a method
class Car_3:
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

    # added a method to update attribute value
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


old_car = Car_3("audi", "a4", 2024)
print(old_car.get_descriptive_name())

old_car.read_odometer()

# modifying value through method
old_car.update_odometer(16)
old_car.read_odometer()

old_car.update_odometer(31)
old_car.read_odometer()


# 3. Incrementing through a method
class Car_4:
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

    # method to increment value
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


my_used_car = Car_4("subaru", "outback", 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

# using the method to increment value
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
