# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Extras: If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by
# (check). If check divides evenly into num, tell that to the user. If not, print a different
# appropriate message.

num = int(input("Tell me an integer: \n"))
check = int(input("And one more integer to divide the first by: \n"))

if num % check == 0 and num % 4 == 0:
    print(
        "Your first integer, "
        + str(num)
        + ", is even. It is a multiple of four. "
        + str(num)
        + " / "
        + str(check)
        + " leaves no remainder."
    )
elif num % check == 0 and num % 2 == 0:
    print(
        "Your first integer, "
        + str(num)
        + ", is even. "
        + str(num)
        + " / "
        + str(check)
        + " leaves no remainder."
    )
elif num % check == 0 and num % 2 != 0:
    print(
        "Your first integer, "
        + str(num)
        + ", is odd. "
        + str(num)
        + " / "
        + str(check)
        + " leaves no remainder."
    )
elif num % check != 0 and num % 2 == 0:
    print(
        "Your first integer, "
        + str(num)
        + ", is odd. "
        + str(num)
        + " / "
        + str(check)
        + " leaves a remainder."
    )
else:
    print(
        "Your integer, "
        + str(num)
        + ", is odd. "
        + str(num)
        + " / "
        + str(check)
        + " leaves a remainder."
    )

    # TODO? Solution is only 14 lines: https://www.practicepython.org/solution/2014/02/15/02-odd-or-even-solutions.html
