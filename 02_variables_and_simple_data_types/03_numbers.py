# Integers
num1 = 4
num2 = 2

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

# two asterick to represent exponents

print(num1 ** num2)

# BODMAS
print(2 + 3 * 4)
print((2+3)*4)
# spacing doesnt matter


print("")
# Floats
# Any number with a decimal point

num3 = 0.2
num4 = 0.1

# arbitary number of decimal points
print(num3 + num4)
print(num3 - num4)
# arbitary number of decimal points
print(num3 * num4)
print(num3 / num4)


print("")
# Integers and Floats
num1 = 4
num2 = 2

# when you divide any two numbers even if they are integers you get float
print(num1 / num2)

# mixing integetrs and float will result in float
num3 = 6.0

print(num1 + num3)
print(num1 * num3)

# deaults to float when a float is used in an operation, even if answer is whole number


print("")
# Underscores in numbers
# you can use underscores to improve readability. any format can be used
# python ignore these underscores

universe_age = 14_000_000_000
print(universe_age)


print("")
# Multiple Assignments

# multiple varaibles can be assigned value in the same line

# seperate them using comma
x, y, z = 1, 2, 3

# number of variables and valeus should be equal otherwise error
# a, b, c = 1, 2


print("")
# Constants
# Constants: Varibale whose value doesn't change

# python doesn't have built in constatns so progammers use all caps to indiate to treat variable as const
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

# it can still be changed, sicne python doesnt have constants
MAX_CONNECTIONS = 10_000
print(MAX_CONNECTIONS)
