spam = ["cat", "dog", "bat"]
spam.append("moose")
print(spam)

# .append() method will add list item to end of list

spam = ["cat", "dog", "bat"]
spam.insert(1, "chicken")
print(spam)

# insert(x,) allows you to control where list value goes

spam = ["cat", "bat", "rat", "elephant"]
spam.remove("bat")
print(spam)

# remove() lets you specify value rather than index you want removed
# will only remove first instance of value in list

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

# sort() will place integers in order

spam = ["ants", "cats", "dogs", "badgers", "elephants"]
spam.sort()
print(spam)

# Will place strings in alphabetical order

spam = ["ants", "cats", "dogs", "badgers", "elephants"]
spam.sort(reverse=True)
print(spam)

# .sort() can be passed a keyword argument which takes a boolean value
# cannot sort ints and strs together

spam = ["Alice", "Bob", "ants", "badgers", "Carol", "cats"]
spam.sort()
print(spam)

# sort() is ascii-betical, so capital letters go before lowercase

spam = ["a", "z", "A", "Z"]
spam.sort(key=str.lower)
print(spam)

# This sorts in true alphabetical order using key=str.lower
