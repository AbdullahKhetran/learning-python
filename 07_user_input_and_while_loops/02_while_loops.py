# while loop runs as long as a certain condition is true

# counting using while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


print("")
# letting user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'q' to end the program. "

message = ""
while message != "q":
    message = input(prompt)
    # we dont want the quit value to be printed
    if message != "q":
        print(message)


print("")
# Using a flag
# For a program that should run only as long as many conditions are
# true, you can define one variable that determines whether or not
# the entire program is active.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'q' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == "q":
        active = False
    else:
        print(message)


print("")
# Using break to exit a loop

prompt = "\nPlease enter the name of city you have visited:"
prompt += "\n(Enter 'q' when you are finished.) "

while True:
    city = input(prompt)

    if city == "q":
        break
    else:
        print(F"I'd love to go to {city.title()}!")

# break keyword can be used in any loop


print("")
# Continue keyword
# continue will return to the beginning of the loop

# printing only odd numbers
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        # go back to start of loop
        continue

    print(current_number)


print("")
# Avoiding infinite loops
# Make sure at least one part of the program can make
# the loop’s condition False or cause it to reach a break statement.

x = 1
# the condition
while x < 5:
    print(x)
    # if next line is omitted it will be infinite loop
    x += 1
