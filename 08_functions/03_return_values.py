# the value that a function returns is called a return value


# Returning a simple return value
def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)


# Optional Argument
# empty default value, move to end of parameter list
def return_greeting(first_name,  last_name, middle_name=""):
    """Return a greeting message with neatly formatted full name"""
    message = f"\nWelcome {first_name} {middle_name} {last_name}"
    return message.title()


musician = return_greeting("john", "hooker", "lee")
print(musician)

# works without middle name
musician = return_greeting("john", "hooker")
print(musician)
# but there is an additional space in output
# to remove that middle_name variable should not be in return statement


def return_greeting2(first_name,  last_name, middle_name=""):
    """Return a greeting message with neatly formatted full name"""
    if middle_name:
        message = f"\nWelcome {first_name} {middle_name} {last_name}"
    else:
        # middle_name is not in return statement in the case where
        # it is not provided
        message = f"\nWelcome {first_name} {last_name}"
    return message.title()


musician = return_greeting2("john", "hooker")
print(musician)
