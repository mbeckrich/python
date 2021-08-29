eggs = {"name": "Zophie", "species": "cat", "age": 8}

print("`list(eggs.keys())` returns the keys in a dictionary: ")
print(list(eggs.keys()))

print("`list(eggs.values())` returns the values in a dictionary:")
print(list(eggs.values()))
print("`list(eggs.items())` returns the items in a dictionary as paired tuples.")
print(list(eggs.items()))

print(
    "These methods return 'list-like' data types: `dict_key`. You have to pass a list",
    "value to these methods to return an actual list: list()",
)
