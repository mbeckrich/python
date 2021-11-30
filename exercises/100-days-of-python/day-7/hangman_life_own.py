# Step 4

import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess in display:
        print(f"{stages[6]}")

    if guess not in display:
        lives -= 1
        if lives == 0:
            print(f"{stages[0]}\n You have lost.")
            exit()
        if lives < 6:
            print(f"{stages[lives]}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

# Differences in her code:
# 1) Uses 'if guess not in chosen_word'
# My way doesn't seem to produce any problems but might be less
# logical.
# 2) She uses end_of_game = True instead of exit(), but maybe because
# she hasn't taught exit().
# 3) She uses print(f"{stages[lives]}" which I do as well but in a less
# efficient place I think?)
