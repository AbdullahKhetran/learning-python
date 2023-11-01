motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# modifying element
motorcycles[0] = "ducati"
print(motorcycles)

# adding elements
motorcycles.append("honda")

cars = []
cars.append("suzuki")
cars.append("honda")
cars.append("toyota")
print(cars)

# inserting  at specific index
cars.insert(1, "kia")
print(cars)

# deleting element
del motorcycles[1]
print(motorcycles)

# unlike del, pop returns the value so you can store it in variable and use

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# popping fro specific index
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}")

# removing usign value
years = ["2000", "2001", "2002", "2003"]
print(years)

years.remove("2000")
print(years)

# it returns the value just like pop

remvoed_year = years[1]
print(f"The removed year is {remvoed_year}")

# The remove() method deletes only the first occurrence of the value you specify. For all values use a loop
