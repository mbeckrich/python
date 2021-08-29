eggs = {"name": "Zophie", "species": "cat", "age": 8}

# Long way to put a key into a dictionary
if "color" not in eggs:
    eggs["color"] = "black"  # two lines

# Cleaner way
eggs = {"name": "Zophie", "species": "cat", "age": 8}

eggs.setdefault("color", "black")  # one line

print(eggs)

# If setdefault() is used again with the color key and
# different value, the original dict value of black will not
# change.
