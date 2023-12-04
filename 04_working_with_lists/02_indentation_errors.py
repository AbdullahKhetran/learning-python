# Python uses indentation to determine how a line, or group of lines,
#  is related to the rest of the program.

# Forgetting to indent
magicians = ['alice', 'david', 'carolina']
# this will result in error, since line is not indented
# for magician in magicians:
# print(magician)


# forgetting to indent additional lines
for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
# next line is not indented even though it was supposed to. But still no error
# cause syntax is valid. this is logical error
print(f"I can't wait to see your next trick, {magician.title()}.\n")


# Indenting unnecessarily
message = "Hello python"
# will error if indented
# print(message)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I cant wait to see your next trick, {magician.title()}.")

# logical error: unnessory indentation
    print("Thank you everyone")


# forgettign colon
# this will result in error sicne colon is missing
# for magician in magicians
#     print(magician)
