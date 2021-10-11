# Round floats using round()
# e.g. print(round(8 / 3, 2)) rounds to two decimal places
# Floor division can be used to avoid floats, will return an int
# e.g. print(8 // 3)
# variables to be operated on later can be changed simply:
# score = print(8 * 3) # 24
# score += 2 # or -=, *=, /=
# print(score) # is now 26

# f string on int, float, boolean

score = 0
height = 1.8
isWinning = True

print(
    f"your score is {score}, your height is {height}, and you are",
    f"winning is {isWinning}.",
)  # f"" makes it an f-string
