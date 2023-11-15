# Positional Arguments
# passing with the same SAME the parameter were provided

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


describe_pet("hamster", "harry")

describe_pet("dog", "willie")

# order matters
# wrong order, result doesnt make sense
describe_pet("harry", "hamster")


# Keyword Arguments
# name-value pairs that you can pass in any order

describe_pet(animal_type="hamster", pet_name="harry")


# Default values
# a default value can be assigned in function defination

# default value parameters have to be listed in the end so that
# python can interpret positional arguments correctly
def describe_pet2(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


describe_pet2("willie")

# not using default
describe_pet2("harry", "hamster")


# Equivalent postional calls
# multiple ways to call function espically if default value is used
def describe_pet3(pet_name, animal_type="dog"):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


# dog named Willie.
describe_pet3("willie")
describe_pet3(pet_name="willie")

# hamster named Harry.
describe_pet3("harry", "hamster")
describe_pet3(pet_name="harry", animal_type="hamster")
describe_pet3(animal_type="hamster", pet_name="harry")


# Avoiding argument errors

# if you provide less or more arguments then you will get error

def describe_pet4(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# errors
# describe_pet4() # missing
# describe_pet4("hamster") # still missing
# describe_pet4("hamster", "harry", "friendly")  # additional

# correct
describe_pet4("hamster", "harry")
