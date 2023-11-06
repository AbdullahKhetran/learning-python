bicycles = ["trek", "cannodale", "redline", "specialized"]
print(bicycles)

# accessing elements in a list
# listName[number]

print(bicycles[0])

# using method applicable on string
print(bicycles[0].title())

# index starts at 0 not 1
print(bicycles[1])

# Negative index
# to access the last item in the last, start from -1
print(bicycles[-1])

# using it as variable
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
