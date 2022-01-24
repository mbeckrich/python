import random


def random_number():
    """Returns a random number to be guessed by the player."""
    number = random.choice([n for n in range(1, 101)])
    return number


difficulty = input(
    "Choose your difficulty: type 'easy' for 10 guesses and 'hard' for 5"
    " guesses. "
)


def guesses():
    """Provides countdown for difficulty modes."""
    guesses_remaining = 0
    if difficulty == "easy":
        guesses_remaining += 10
    if difficulty == "hard":
        guesses_remaining += 5
    return guesses_remaining


computer_number = random_number()
guesses_remaining = guesses()


def game_loop():
    """Takes input from players depending on difficulty and guesses remaining.
    It provides a different prompt on your first guess.
    """
    if difficulty == "easy" and guesses_remaining == 9:
        return int(input("Go ahead and guess a number: "))
    if difficulty == "hard" and guesses_remaining == 4:
        return int(input("Go ahead and guess a number: "))
    else:
        return int(input("One more guess? "))


def win_con(guess):
    """This checks to see if the player's guess has met the game's win
    condition."""
    if guess == computer_number:
        print("You guessed the number!")
        exit()
    elif guess > computer_number:
        if guesses_remaining == 0:
            print(
                "Still too high and you're of guesses -- better luck next"
                " time!"
            )
            exit()
        else:
            print(f"Too high! You have {guesses_remaining} tries left.")
    elif guess < computer_number:
        if guesses_remaining == 0:
            print(
                "Still too low and you're out of guesses -- better luck next"
                " time!"
            )
            exit()
        else:
            print(f"Too low! You have {guesses_remaining} tries left.")


while guesses_remaining != 0:
    guesses_remaining -= 1
    win_con(game_loop())

# differences in her code:
# checks answer
# def check_answer(guess, answer)
# if guess > answer:
# difficulty set
# uses global constant for number of guesses
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
# def set_difficulty():
#     level = input("Choose a difficulty")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS
