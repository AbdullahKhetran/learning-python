print("Python")

# add a tab with \t
print("\tPython")

# add a new line with \n
print("Languages:\nPython\nC\nJavascript")

# both newlines and tab
print("Languages:\n\tPython\n\tC\n\tJavascript")


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
