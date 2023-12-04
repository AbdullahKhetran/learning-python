# alias to class
from car import ElectricCar as EC
# alais to module
import car as ec

my_leaf = EC("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

leaf = ec.ElectricCar("nissan", "leaf", 2024)
print(leaf.get_descriptive_name())
