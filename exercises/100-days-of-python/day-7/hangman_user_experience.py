# Step 5

import random
import hangman_art
import hangman_words

# Can write `from hangman_words import word_list`
# and `from hangman_art import stages, logo`

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f"{hangman_art.logo}")

# Testing code
# print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n"
        #     f" Guessed letter: {guess}"
        # )
        if letter == guess:
            if guess in display:
                print(f"You have already guessed {guess}!")
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word. The noose tightens!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
