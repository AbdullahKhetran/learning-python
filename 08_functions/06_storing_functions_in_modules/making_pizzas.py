import pizza
# whole module imported
from pizza import make_pizza

# module_name.function_name()
pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# Importing specific functions

# from module_name import function_name
# from module_name import function_0, function_1, function_2

# import statement automatically shifted on top on saving file
make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# Alias for function
# just add 'as nickname' in the import statement
# from module_name import function_name as fn


# Alias for module
# import module_name as mn


# Import all functions from a module
# from module_name import *
# best not to use this approach because of name conflicts
# Python will overwrite the functions if there is a conflict
