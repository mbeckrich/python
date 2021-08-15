name = "Alice"
if name == "Alice":
    print("Hi Alice")
print("Done")

# If name is False, indented code is ignored

name = "Bob"
if name == "Alice":
    print("Hi Alice")
print("Done")

# Truthy and falsey values don't use == evaluations, but can still be used in `if`
# and `else` lines like the below. This code works, but `if name != '':` is cleaner and safer.
# 0 is falsey, all others are truthy. 0.0 is falsey, all others are truthy. e.g. bool(0) function
# is a falsey value. bool() can be used to test which values are truthy and falsey.


print("Enter a name.")
name = input()
if name:
    print("Thank you for entering a name.")
else:
    print("You did not enter a name.")
