from typing import TypedDict

# A dictionary is a collection of key-value pairs

# when you provide a key, python returns its value


# Accessing values in a dictionary

alien = {"color": "green"}

# name_of_dictionary[key]

value = alien["color"]
print(value)

alien_0 : dict[str, str | int] = {"color": "green", "points": 5}
new_points = alien_0["points"]
print(f"You just earned {new_points} points!")


# Adding new key-value pairs
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)


# Starting with an empty dictioanary
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)
# empty dictionaries are useful when user-supplied data is stored


print("")
# Modifying values


class Alien(TypedDict):
    x_position: int
    y_position: int
    speed: str


alien_0 = {"color": "green"}
print(f"The alien is {alien_0['color']}")

alien_0 = {"color": "yellow"}
print(f"The alien is now {alien_0['color']}")

print("")
alien_1: Alien = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original x-position: {alien_1['x_position']}")

if alien_1["speed"] == "slow":
    x_increment = 1
elif alien_1["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

# new position = old position + increment
alien_1["x_position"] = alien_1["x_position"] + x_increment

print(f"New x-position: {alien_1['x_position']}")


print("")
# Removing key-value pairs

# you need to use del statement

alien_0 = {"color": "green", "points": 5}
print(f"before removeing: {alien_0}")

del alien_0["points"]
print(f"after removeing: {alien_0}")

# deleting it is permenant


print("")
# Dictionary of similar objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}")


print("")
# Using get() to access values
# if the key doesnt exist in dictionary and you try to access it you
#  will get an error
# get() method is used to define a value to be returned in such case

alien_0 = {"color": "green", "speed": "slow"}
# error
# print(alien_0["points"])

# get(key, value to be returned)
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

# value to be returned is optional, if not provided default is None
