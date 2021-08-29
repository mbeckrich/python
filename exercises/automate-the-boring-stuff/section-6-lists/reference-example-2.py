def eggs(cheese):
    cheese.append("Hello")


spam = [1, 2, 3]
eggs(spam)
print(spam)

# Example of mutable value, where eggs(spam) adds
# "Hello" to list rather than ignoring it
# Any modification to a list will affect all forms of the list
