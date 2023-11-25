def greet_users(names: list[str]) -> None:
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)


# Modifying a list in a function
def print_models(unprinted_designs: list[str], completed_models: list[str]) -> None:
    """
    Simulate printing each desing, until none are left
    Move each desing to completed_models after printing
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models: list[str]) -> None:
    """Show all the models that we printed."""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models: list[str] = []

print(
    f"""
Lists before functions:
    Unprinted designs: {unprinted_designs}
    Completed models: {completed_models}
    """)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print(
    f"""
Lists after functions:
    Unprinted designs: {unprinted_designs}
    Completed models: {completed_models}
    """)

print("Orignal lists have been modified")


# Preventing a function from modifying a list
# just pass a copy of list
# syntax: function_name(list_name[:])

unprocessed_designs = ["phone", "robot", "lms"]
processed_designs: list[str] = []

print_models(unprocessed_designs[:], processed_designs[:])
show_completed_models(completed_models)
# original list is still unmodifed
print(f"Original list after function: {unprocessed_designs}")
