print(
    "Another string method is 'join()', which combines a series of strings into a list. For example, "
    + ".join(['cats', 'bats', 'rats'])) will return:",
    ",".join(["cats", "bats", "rats"]),
    "The ',' string is what Python uses to separate the string items.",
    "If you used ', ', the string would look nicer. See:",
    ", ".join(["cats", "bats", "rats"]) + ".",
    "Strings could also use the new line character and format like so:\n"
    + "\n".join(["cats", "bats", "rats"]),
)
print(
    "The split() method does the opposite. For example, 'My name is Simon'.split() will return:",
    "My name is Simon".split(),
)

print(
    ".split() can be passed arguments to split on specific characters. For example, 'My name is Simon.split(n) will produce:",
    "My name is Simon".split("n"),
    "The 'n' character disappears and each string is separated into a list from 'n.'",
)
