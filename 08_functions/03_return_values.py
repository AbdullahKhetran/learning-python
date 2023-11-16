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
    full_name = f"\nWelcome {first_name} {middle_name} {last_name}"
    return full_name.title()


musician = return_greeting("john", "hooker", "lee")
print(musician)

# works without middle name
musician = return_greeting("john", "hooker")
print(musician)
