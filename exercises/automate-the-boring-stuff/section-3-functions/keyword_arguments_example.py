# print() places a new line after function call
print("hello")
print("world")

# this uses keyword argument "end" to add a blank string between print()s
print("hello", end="")
print("world")

# this will add spaces between each string as they are printed
print("cat", "dog", "mouse")

# this uses the `sep` keyword argument to change what separates each printed string
print("cat", "dog", "mouse", sep="ABC")

# keyword arguments are often unnecessary. `print()` has keyword arguments `end` and `sep`
