# Can think of a string as list-like, in that each item in a string
# can be thought of as a list item. e.g. 'Hello world!' as
# [H], [e], [l], etc.

spam = "Hello world!"
print("spam[0] will return Hello world!'s index 0:", spam[0])

print("Similarly, a slice can be performed. As spam[1:5] shows:", spam[1:5])

print("`in` and `not in` can also be used. `'Hello' in spam` returns:", "Hello" in spam)
