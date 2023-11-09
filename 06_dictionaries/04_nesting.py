# A list of dictionaries
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# empty list for storing aliens
aliens = []

# generating 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# print first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

# changing first 3 aliens
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")


print("")
# A list in a dictionary

pizza = {
    "crust": "thick",
    # list inside a dictionary
    "toppings": ["mushrooms", "extra cheese"],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

# do this when you want more than one value to be
# associated with a single key

favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# You should not be nesting lists and dictionaries too deeply


print("")
# Dictionary inside a dictionary
# you can do this but code will become complicated quickly

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton"
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # constructuing full name
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# In this case structure of each user's dictionary was same.
# this makes nested dictionaries easier to work with
# If keys were different, then code inside for loop
# would be more complicated
