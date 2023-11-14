def greet_user():
    # docstring: describes what the function does
    """Display a simple greeting."""
    print("Hello!")


greet_user()


print("")
# Passing information to a function


def greet_user_2(username: str):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}")


greet_user_2("jesse")
greet_user_2("sarah")


print("")
# Arguments and parameters
# parameter: information inside the definatination
# argument: information while calling function
