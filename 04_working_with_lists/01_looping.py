magicians = ['alice', 'david', 'carolina']
# for every magician in magicians list
for magician in magicians:
    # print the magician's name
    print(magician)

# naming covnention: for item in list_of_items

for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    # every indented line is condsidered inside the loop
    print(f"I cant wait to see your next trick, {magician.title()}.\n")

# since this is not indented its outside the loop
print("Thank you everyone. That was a great magic show")
