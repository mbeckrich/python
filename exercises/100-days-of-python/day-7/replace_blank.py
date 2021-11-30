# Step 2

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

guess = input("Guess a letter: ").lower()

display = []

for letter in range(len(chosen_word)):
    # display.append("_")
    display += "_"
print(display)  # Shows _ in list, replace with letter

# Her code is:
# for letter in range(len(chosen_word)):
#   display += "_" <-- Difference, doesn't append
# print(display)

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
