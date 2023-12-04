from pathlib import Path

path = Path('pi_digits.txt')

contents = path.read_text()
print(contents)

contents_2 = path.read_text().rstrip()
print(contents_2)


# Accessing a File’s Lines
lines = contents.splitlines()
for line in lines:
    print(line)
