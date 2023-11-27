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

    def __init__(self, make: str, model: str, year: int) -> None:
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        """Return a neatly formattted descriptive name"""
        long_name = f"\n{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self) -> None:
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage: int) -> None:
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles: int):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


# child class
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())


# Defining Attributes and Methods for the Child Class
class ElectricCar2(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self) -> None:
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")


my_leaf_2 = ElectricCar2("nissan", "leaf", 2024)
print(my_leaf_2.get_descriptive_name())
my_leaf_2.describe_battery()


# Overriding Methods from the Parent Class

# lets say Car class has a fill_gas method. This is not applicable on
# electric car so it need to be override

class ElectricCar3(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self) -> None:
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def fill_gas_tank(self) -> None:
        """Electric cars dont have gas tanks"""
        print("This car doesnt have a gas tank!")


my_leaf_3 = ElectricCar3("nissan", "leaf", 2024)
print(my_leaf_3.get_descriptive_name())
my_leaf_3.describe_battery()
my_leaf_3.fill_gas_tank()


# Instances as Attributes
# Composition: breaking large class into smaller classes

# smaller class
class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=40) -> None:
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self) -> None:
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self) -> None:
        """Print a statement about the range this battery provides"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")


class ElectricCar4(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Initialize attributes of the parent class
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        # smaller class is used in larger class
        self.battery = Battery()


my_leaf_4 = ElectricCar4("nissan", "leaf", 2024)
print(my_leaf_4.get_descriptive_name())
my_leaf_4.battery.describe_battery()
my_leaf_4.battery.get_range()
