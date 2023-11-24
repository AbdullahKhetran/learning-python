# set of modules included with every Python installation.

from random import randint, choice

# radint generates a random number
random_number = randint(1,6)
print(random_number)

# choice takes in list or tuple and returns a randomly chosen element
players = ["charles","martina","michael","florence","eli"]
first_up = choice(players)
print(first_up)

# random module shouldn’t be used when building security-related applications