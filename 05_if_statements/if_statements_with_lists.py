requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


print("\n")
# What if certain topping is unavailables

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making pizza")


print("\n")
# checking if a list is not empty
requested_toppings = []

# When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")

    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


# Using multiple lists
available_toppings = ["mushrooms", "olives",
                      "green peppers", "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
else:
    print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
