hello = list("hello")
print(hello)

# str can sometimes be thought of
# as a list of single character strings

# Functions on lists can be used on strings as well
name = "Zophie"
print(name[0])
print(name[1:3])
print(name[-2])
print("Zo" in name)
print("xxx" in name)
for letter in name:
    print(letter)

# The biggest difference between list and string is
# that lists are mutable (can be changed, added to, etc.)
# and strings are immutable (cannot be changed)

# Example:
# name = "Zophie the cat"
# print(name[7] = "X") will not replace t with X, because
# name variable is a string, therefore immutable
