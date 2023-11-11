# while loop runs as long as a certain condition is true

# counting using while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


# letting user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != "quit":
    message = input(prompt)
# we dont want the quit value to be printed
    if message != "quit":
        print(message)
