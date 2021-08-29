spam = {12345: "Luggage combination", 42: "The Answer"}

# Dictionaries are unordered, unlike lists. e.g.
print("[1, 2, 3]" == "[3, 2, 1]")
print(
    "This is false, because, while the integers are the same, lists are",
    "ordered and are evaluated in their order, not just content.",
)

eggs = {"name": "Zophie", "species": "cat", "age": 8}
ham = {"species": "cat", "name": "Zophie", "age": 8}

print(
    "eggs == ham is "
    + str(eggs == ham)
    + ", because dictionaries do not care about order,",
    "just content.",
)

# Key: value pair is like a real dictionary -- if you know the word ('key'),
# you can get the definition ('value').

print(
    "`in` and `not in` work with dictionaries, so name in `eggs` is "
    + (str("name" in eggs))
    + "."
)

# Dictionaries are mutable. They hold reference values, like lists.
