from typing import TypedDict, Optional

# the value that a function returns is called a return value


# Returning a simple return value
def get_formatted_name(first_name: str, last_name: str) -> str:
    """Return a neatly formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)


# Optional Argument
# empty default value, move to end of parameter list
def return_greeting(first_name: str,  last_name: str, middle_name: str = "") -> str:
    """Return a greeting message with neatly formatted full name"""
    message = f"\nWelcome {first_name} {middle_name} {last_name}"
    return message.title()


# middle_name argument should be last to match order of parameters
musician = return_greeting("john", "hooker", "lee")
print(musician)

# works without middle name
musician = return_greeting("john", "hooker")
print(musician)
# but there is an additional space in output
# to remove that, middle_name variable should not be in return statement


def return_greeting2(first_name: str,  last_name: str, middle_name: str = "") -> str:
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


# Returning a dictionary
def build_person(first_name: str, last_name: str) -> dict[str, str]:
    """Returns a dictionary of information about a person"""
    person = {"first": first_name, "last": last_name}
    return person


musician2 = build_person("jimi", "hendrix")
print(f"\n{musician2}")


class Person(TypedDict):
    first: str
    last: str
    age: Optional[int]


def build_person2(first_name: str, last_name: str, age: int | None = None) -> Person:
    """Return a dictionary of a person's information"""
    person: Person = {"first": first_name, "last": last_name, "age": None}
    # if age was provided, add it to the dictionary
    if age:
        person["age"] = age
    return person

# 'None' is used when a variable has no value assigned to it
# it evaluates to false in conditional tests


musician3 = build_person2("jimi", "hendrix", 27)
print(f"\n{musician3}")


# Using a function with a while loop
# while True:
#     print("\nPlease enter your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")

#     # calling function declared on top
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}")
# but this is an infitnite loop, since there is no exit condition


while True:
    print("\nEnter your name")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
