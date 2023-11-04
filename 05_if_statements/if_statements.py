# Simple if statement

# if conditional_test:
#     do something

age = 19
if age >= 18:
    print("You are old enough to vote")

# Indentation matters

# if test passes all indented lines will be executed
age_2 = 17
if age_2 < 18:
    print("You are not old enough to vote")
    print("You will become eligible to vote once you are 18 years old")

# if test fails all indented lines will be ignored
if age_2 >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")


print("\n")
# if-else statements
# one action if condition passes and other for all other cases

if age_2 >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("You are not old enough to vote")
    print("You will become eligible to vote once you are 18 years old")


print("\n")
# if-elif-else Chain
# useful when checking for more than 2 situations
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40s")

# setting price and then printing
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# You can use as many elif blocks
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# Omitting the else block
# the else block is not required
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
    # else block is omitted
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

# else block is a catchall statement. It can run even if there was invalid or malicious data
# so prefer to use a final elif block


print("\n")
# Testing multiple conditions
# if-else or if-elif-else is suitable when you need one test to pass
# when a test passes the rest block are ignored
# to check all conditions use multiple if block

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese")

print("Finished making pizza")

# this would not work as expected if elif was used
# because it would stop when first condition was met
print("\n")
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("Finished making your pizza!")


# objective -> usage
# one block of code to run -> if-elif-else
# multiple block of code to run -> if chain
