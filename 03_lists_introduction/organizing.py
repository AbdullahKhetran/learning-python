# permenant sorting: sort()
cars = ["bmw", "audi", "toyota", "suzuki"]
print("before sort", cars)
cars.sort()
print(f"after sort {cars}")

# reverse order
cars.sort(reverse=True)
print("reverse sort", cars)


# temporary sorting: sorted()
cars2 = ["bmw", "audi", "toyota", "suzuki"]
print("original list", cars2)

modified_list = sorted(cars2)
print("sorted list", modified_list)

print("original list remains unchanged", cars2)


# Note: Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase.

# making list in reverse order: permenant
cars3 = ['bmw', 'audi', 'toyota', 'subaru']

print("cars3 before reverse", cars3)
cars3.reverse()
print("cars3 after reverse", cars3)

# reverse doesnt sort backward alphabectically. It just reverses the order of list


# finding the length of list: len(list)
print("cars length:", len(cars))
