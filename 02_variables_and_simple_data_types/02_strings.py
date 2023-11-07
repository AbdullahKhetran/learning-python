name = "ada lovelace"

# Changing case in a string
print(name.title())
print(name.lower())
print(name.upper())

print("")
# using variables in strings
first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)


print("")
# Adding whitespace
print("Python")

# add a tab with \t
print("\tPython")

# add a new line with \n
print("Languages:\nPython\nC\nJavascript")

# both newlines and tab
print("Languages:\n\tPython\n\tC\n\tJavascript")


print("")
# Stripping Whitespaces
# right side: .rstrip()
# left side: .lstrip()
# both sides: .strip()

favorite_language = "python "
print(favorite_language)

print(favorite_language.rstrip())

# original value remains unchanges unless you reassign it

favorite_language = favorite_language.rstrip()
print(favorite_language)

language = " C "
print(language.rstrip())
print(language.lstrip())
print(language.strip())


print("")
# Removing prefixes
nostarch_url = "https://nostarch.com"
simple_url = nostarch_url.removeprefix("https://")

print(simple_url)

# original value remains unchanged, methods returns a new value
print(nostarch_url)


print("")
# Avoiding syntax error
message = "One of python's strengths is its diverse community."
print(message)

# error here, since single quote inside single quote
# wrong_message = 'One of python's strengths is its diverse community.'
