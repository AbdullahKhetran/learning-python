from pathlib import Path

path = Path("programming.txt")
# write_text() method
path.write_text("I love programming.")

# python can only write string into a file


# Writing Multiple Lines

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)

# if the file already exits, write_text() will replace the content