# Code will produce an error if someone enters a string w/o numeric digits (e.g. 'six')
print("How many cats do you have?")
numCats = input()
if int(numCats) >= 4:
    print("That is a lot of cats.")
else:
    print("That is not that many cats.")
