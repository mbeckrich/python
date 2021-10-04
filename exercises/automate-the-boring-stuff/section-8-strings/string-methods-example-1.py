# Strings are immutable, so methods cannot modify them

spam = "Hello world!"
print(spam.upper())  # Displays spam in all uppercase
print(spam)  # spam itself remains as originally formatted

# To change underlying spam variable
spam = spam.upper()
print(spam)

# lower() method does the same for lowercase

# Practical example:

print("Would you like to play again? ")
answer = input()

# Wrong

"""
if answer == "yes":
    print("We'll play again, then.")  # Problem here if player says 'YES'
if answer == "no":
    print("Bye!")
"""
# Instead

if answer.lower() == "yes":
    print("We'll play again, then.")
elif answer.lower() == "no":
    print("Bye!")
elif answer.lower() != "yes" or "no":
    print("Say 'yes' or 'no' only, please!")
