# strings are fixed in time to their variable, example:

spam = 42
cheese = spam
spam = 100
print(spam)  # 100
print(cheese)  # cheese remains fixed at 42

# lists are assigned to variables as a reference

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "Hello"
print(cheese)
print(spam)  # produces same thing
# cheese and spam are both pointing to the same reference,
# so reference is what is being manipulated
# when spam is assigned to cheese, cheese is getting
# reference value rather than immutable string
# Immutable values can't be modified 'in place,'
# they can only be replaced by new values.
# Further explanation from Ned Batchelder:
# http://youtu.be/_AEJHKGk9ns
