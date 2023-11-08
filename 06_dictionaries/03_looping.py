# Looping through all key-value pairs
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# key and value can be given any name, these are just variables used
# to store value of key and value
# This would also work `for k, v in user_0.items()`

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")


print("")
# Looping through all the keys
# .keys() method

for name in favorite_languages.keys():
    print(name.title())

# .keys() is default method for looping on dictionaries so you can even
# skip it and write like this `for name in favorite_languages:`

print("")
for name in favorite_languages:
    print(name.title())

print("")
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")


print("")
# Looping through keys in a particular order
# sorted() method

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

# here all the keys were sorted before running the loop


print("")
# Looping through all values
# values() method
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
# but this shows even the repeated ones in this case python

# set() is used to get only unique
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


# Sets
languages = {"python", "rust", "python", "c"}
# looks like dicitonary but no key-value pair
# note python will be de-duplicated
print(languages)
