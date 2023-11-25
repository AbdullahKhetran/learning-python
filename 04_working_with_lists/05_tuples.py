# Tuple: An list that cannot be modified (immutable list)
# parentheses are used instead of square brackets

# lets say a rectange that should alwyas be of a certain size
dimensions = (200, 50)
print(
    f"Rectangle has following dimensions:\nHeight: {dimensions[0]}\nWidth:{dimensions[1]}")

# this will error
# dimensions[0] = 250


# Note: Tuples are technically defined by absence of square brackets.
# Parentheses are used to make them more readable
# This is a valid tuple
triangle = 3, 4, 5
print(f"triangle tuple: {triangle}")

# But if you want a tuple of only 1 element the use a trailing comma otherwise 
# it will be treated as a variable

# tuple
circel_radius = 4,
print(f"Circle tuple: {circel_radius}")
# variable
circe_diameter = 8
print(f"circle tuple but a variable due to absence of comma: {circe_diameter}")


# loop on tuple
for dimension in dimensions:
    print(dimension)


# "over-riding" tuple
# by assigning a new value to the variable that represents the tuple, we have reassigned the tuple which is valid
numbers = (21, 22)
print("\noriginal numbers")
for number in numbers:
    print(number)

numbers = (45, 47)
print("\nmodified numbers")
for number in numbers:
    print(number)
