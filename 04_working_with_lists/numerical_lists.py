# range() function generate a series of numbers

for value in range(1, 5):
    print(value)
# last value is exclusive

# 0 is default first argument (starting value)
for value in range(3):
    print(value)


# making list using range()
# list() function will be used alognside range()
numbers = list(range(1, 6))
print(numbers)

# step argument to range(). 3rd argument
even_numbers = list(range(2, 11, 2))
# each generated number is an step of 2. default step is 1
print(even_numbers)

squares: list[int] = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


# simple statstics
digits = list(range(0, 11))
smallest = min(digits)
largest = max(digits)
total = sum(digits)
print(f"smallest number: {smallest}")
print(f"largest number: {largest}")
print(f"total number: {total}")


# list comprehensions

squares_list = [value**2 for value in range(1, 11)]
print(f"squares using list comprehension: {squares_list}")
