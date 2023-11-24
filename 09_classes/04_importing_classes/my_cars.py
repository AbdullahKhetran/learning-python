# Importing Multiple Classes from a Module
from car import Car, ElectricCar

# Importing an Entire Module
import car

# Importing All Classes from a Module
# from module_name import *
# this is not recommended because of name conflicts


# using multiple classes from a module
my_mustang = Car("ford","mustang",2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar("nissan","leaf",2024)
print(my_leaf.get_descriptive_name())


# using an entire module
mustang = car.Car("ford","mustang",2024)
print(mustang.get_descriptive_name())

leaf = car.ElectricCar("nissan","leaf",2024)
print(leaf.get_descriptive_name())