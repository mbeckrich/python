print("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("That is a lot of cats.")
    if int(numCats) < 0:  # The 'extra credit' solution to someone entering a neg number
        print("You can't have negative cats!")
    else:
        print("That is not that many cats.")
except ValueError:
    print("You did not enter a number.")
