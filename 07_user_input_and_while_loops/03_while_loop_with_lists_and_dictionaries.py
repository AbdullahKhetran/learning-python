# to modufy a list in a loop use 'while' loop not 'for' loop

# Moving items from one list to another
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users: list[str] = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Displaying confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print("")
# Removing all instances of a specific value
# remvoe() only remove the value once, but we can use it in a loop

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)


print("")
# Filling a dictionary with user input

responses : dict[str, str] = {}
# Setting a flag
polling_active = True

while polling_active:
    # Gathering data
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb? ")

    # storing data
    responses[name] = response

    # more data
    repeat = input("Anyone else? (yes/no) ")
    if repeat == "no":
        # changing flag to stop loop
        polling_active = False

# Displaying results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
