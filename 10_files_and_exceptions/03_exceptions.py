# Exceptions are special objects which python uses to manager errors

# will result in error
# print(5/0)

# Using try-except Blocks
# try-except block handles error gracefully and dosent stop the program
try:
    print(5/0)
except ZeroDivisionError:
    print("You cant divide by zero")

print("code after error")


# Using Exceptions to Prevent Crashes
print("\nGive me two numbers and I'll divide them")
print("Enter 'q' to quit")

flag = True

while flag:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    # try block
    try:
        answer = int(first_number) / int(second_number)
    # except block
    except ZeroDivisionError:
        print("You cant divide by 0!")
    # else block
    else:        
        print(answer)
        flag = False

# code that can cause an error goes to try block
# code to deal with error goes in except block
# code that should run if no error goes in else block 


# Handling the FileNotFoundError Exception

from pathlib import Path

# this file is missing
path = Path("alice.txt")

# this will give error
# contents = path.read_text(encoding="utf-8")

try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"\nSorry, the file {path} does not exist")


# Analyzing text
