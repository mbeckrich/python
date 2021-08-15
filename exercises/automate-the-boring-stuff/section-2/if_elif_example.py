# `if` `elif` executes the first block that evaluates as True and ignores any later statements.
# An `else` statement can be added to the end of the `elif` statements and will be executed if
# all of the `if` `elif` statements are False.

name = "Bob"
age = 3000
if name == "Alice":
    print("Hi Alice")
elif age < 12:
    print("You are not Alice, kiddo.")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")
elif age > 100:
    print("You are not Alice, grannie.")
