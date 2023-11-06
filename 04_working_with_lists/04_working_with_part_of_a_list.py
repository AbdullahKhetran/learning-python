# Slicing a list
players = ["charles", "martina", "michael",
           "florence", "eli", "john", "amy", "amber", "sam"]
print(f"First 3 players are: ${players[0:3]}")
# ending index value is exclusive

print(players[2:4])

# default for 1st arg is 0 index
print(players[:4])
# default for 2nd arg is last index
print(players[1:])

# negative index is also useable
print(f"last 2 players are {players[-2:]}")

# 3rd argument is step. default step is 1
print(players[0:5:2])


# looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


# copying a list

# we can make a copy of list by not providing both 1st and 2nd argument
my_foods = ["pizza", "falafel", "cake"]
# starts at 0 index and ends at last index
friend_foods = my_foods[:]

# now we have two seperate lists.
my_foods.append("chocolate")
friend_foods.append("ice cream")

print(f"I like {my_foods}")
print(f"My friend likes {friend_foods}")
