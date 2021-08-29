eggs = {"name": "Zophie", "species": "cat", "age": 8}

print(
    ".get() method avoids having to use repetitive if statements to prevent errors",
    "accessing dicts",
)
print("eggs.get('age', 0) tells python to get the value for age, else return 0:")
print(eggs.get("age", 0))

print(
    "eggs.get(color, '') will return a blank string if 'color' is not found in the",
    "dict:",
)
print(eggs.get("color", ""))
