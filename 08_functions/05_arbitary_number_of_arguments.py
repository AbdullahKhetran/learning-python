# sometimes you dont know the number of arguments you will want

def print_toppings(*toppings:str) -> None:
    # * indicates collection of arbitary number of arguments
    """Print the list of toppings that have been requested."""
    print(toppings)

# arguments will be stored in a tuple


print_toppings("pepperoni")
# calling function with arbitary number of arguments
print_toppings("mushrooms", "green peppers", "extra cheese")


def add_toppings(*toppings: str) -> None:
    """List the toppings we are adding."""
    print("\nAdding the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


add_toppings("pepperoni")
add_toppings("mushrooms", "green peppers", "extra cheese")


# Mixing positonal and arbitary arguments
# the parameter that collects arbitary number of arguments
# should be placed at the last

def make_pizza(size: int, *toppings: str) -> None:
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# Arbitary key-value pairs
# ** for accepting key-value pairs

def build_profile(first: str, last: str, **user_info:str) -> dict[str,str]:
    # dictionary called user_info will be created
    """Build a dictionary containing everything we know about a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics")

print(user_profile)
