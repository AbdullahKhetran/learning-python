# input() function pauses program and waits for user to enter some text

message = input("Tell me something, and I will repeat it back to you: ")
# note the space after colon
print(message)

# input() takes one argument, that is prompt


# Write clear prompts

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# you can assign prompt to a variable
# this will be useful to construct longer prompts

prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"Hello, {name}!")


# Using int() function
# int() function is used to get numercial value
# input() funtion stores response as string
# int() convert string to numerical value

height = input("How tall are you, in inches? ")
height_int = int(height)

if height_int >= 48:
    print("\nYou are tall enough to ride")
else:
    print("\nGet taller")


# Modulor opertator %

# modulo operator % (percentage sign)
# divides one number by another and return the reaminder

num1 = 4 % 3
num2 = 5 % 2
num3 = 12 % 4
print(num1)
print(num2)
print(num3)

# one use case is to determine whether number is even or odd

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number_int = int(number)

if number_int % 2 == 0:
    print(f"\n The number {number} in even.")
else:
    print(f"\nThe number {number} is odd.")
