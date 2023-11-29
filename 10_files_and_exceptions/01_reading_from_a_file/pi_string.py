from pathlib import Path


# Working with a File's Contents
path = Path('pi_digits.txt')

contents = path.read_text()
lines = contents.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))


# Large Files: One Million Digits
path_2 = Path("pi_million_digits.txt")
contents_2 = path_2.read_text()

lines_2 = contents_2.splitlines()
pi_string_2 = ""

for line in lines_2:
    pi_string_2 += line.lstrip()

print(f"{pi_string_2[:52]}...")
print(len(pi_string_2))

