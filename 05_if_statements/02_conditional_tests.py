# A test that evaluatest to True or False

# Equality Check ==
car = "bmw"
print(car == "bmw")
print(car == "audi")


# Ignoring cases when checking
# test are case sensitive
car2 = "Audi"
print(car == "audi")
print(car2.lower() == "audi")


# Inequality Check !=
# inequality operator is !=
requested_topping = "mushrooms"

if requested_topping != "anchoives":
    print("Hold the anchovies")


# Numerical Comparisons

age = 18
print(age == 18)

answer = 17
if answer != 42:
    print("Wrong answer, try again")

if age < 18:
    print("You are underage")

if age >= 18:
    print("You may enter")


# Checking Multiple Conditions
# "and" & "or" keywords

# "and" evaluates to true only when all the condtions are true
age_0 = 22
age_1 = 18

result = age_0 >= 21 and age_1 >= 21
print(result)

age_1 = 23
result_updated = age_0 >= 21 and age_1 >= 21
print(result_updated)

# You can also use parentheses to improve readability
allowed = (age_0 >= 18) and (age_1 >= 18)
print(f"This group is allowed: {allowed}")

# "or" evaluates to true when any one of the condtions is true
age_3 = 15
age_4 = 24

adult_result = age_3 >= 18 or age_4 >= 18
print(f"We have an adult here: {adult_result}")

kid_result = age_3 < 12 or age_4 < 12
print(f"We have a kid here: {kid_result}")


# Checking whether a values is in a list
# "in" keyword
toppings = ["mushrooms", "onions", "pineapple"]
result_mushroom = "mushroom" in toppings
print(f"Mushroom is in list: {result_mushroom}")

result_cheese = "cheese" in toppings
print(f"Cheese is in list: {result_cheese}")


# Checking whether a value is NOT in a list
# "not" keyword
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response")


# Boolean expressions
# another name if conditional test

game_active = True
is_admin = False
