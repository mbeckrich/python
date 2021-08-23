# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Please tell me your name: \n")  # \n causes a linebreak
print("Thanks! Hi, " + name)

age = int(input("And how old are you, " + name + "? \n"))
print(name + ", you are " + str(age) + " years old.")

i = int(100)
old_age = i - age
print("You will be 100 in " + str(old_age) + " years.")
