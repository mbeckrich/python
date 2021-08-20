# This can't print Thank you! because at the
# end of the `while` block, Python jumps back
# to the start of it. It won't move to Thank you!
# until name = "your name" at the prompt.
# Example of 'input validation,' keeps asking
# for valid input.

name = ""
while name != "your name":
    print("Please type your name.")
    name = input()
print("Thank you!")

# Checks `if` statement, if name == "your name,"
# executes break statement, which causes code to immediately
# leave the loop without rechecking condition.
# `break` helpful in `while` statements.

name = ""
while True:
    print("Please type your name.")
    name = input()
    if name == "your name":
        break
print("Thank you!")
