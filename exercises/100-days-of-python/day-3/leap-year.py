# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

if year % 4 == 0:
    print(
        f"{year} is evenly divisible by four. Now to see if it's evenly",
        "divisible by 100...",
    )
    if year % 100 != 0:
        print(
            f"{year} is not also evenly divisible by 100,",
            "so it is a leap year.",
        )
    elif year % 400 == 0:
        print(
            f"{year} evenly divisble by 100, but it's also evenly divisible",
            "by 400, so it is a leap year.",
        )
    else:
        print(
            f"{year} is evenly divisible by 100, but not 400, so it is not",
            "a leap year. :(",
        )
else:
    print(
        f"{year} is not evenly divisible by four, so it is not a leap year. :("
    )

# Differences from her code:
# 1) She nests if statements rather than using elif.
# Maybe because I used != I was able to use elif?
# She says the if nesting is more readable.
