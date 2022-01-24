from game_data import data
from art import logo, vs
import random

PLAYER_SCORE = 0
PLAY_GAME = True


print(logo)
print(
    "Welcome to the Higher/Lower game. Guess which social media account has"
    " more followers.\n"
)

followers = []


def account_comparision():
    """Generate accounts for comparison."""
    account_info = data[random.randint(0, len(data) - 1)]
    return (
        account_info["name"],
        account_info["description"],
        account_info["country"],
        account_info["follower_count"],
    )


ACCOUNT_ONE = account_comparision()
ACCOUNT_TWO = account_comparision()


def game_loop():
    """Runs the game."""
    global PLAYER_SCORE
    global PLAY_GAME
    global ACCOUNT_ONE
    global ACCOUNT_TWO

    while ACCOUNT_ONE == ACCOUNT_TWO:
        ACCOUNT_TWO = account_comparision()

    print(
        f"Compare A: {ACCOUNT_ONE[0]} is a/an {ACCOUNT_ONE[1]} from"
        f" {ACCOUNT_ONE[2]}."
    )

    print(vs)

    print(f"{ACCOUNT_TWO[0]} is a/an {ACCOUNT_TWO[1]} from {ACCOUNT_TWO[2]}.")

    player_guess = input("Who has more followers? Type 'a' or 'b'.\n").lower()
    if player_guess == "a" and ACCOUNT_ONE[3] > ACCOUNT_TWO[3]:
        PLAYER_SCORE += 1
        print(f"Correct! Your current score is {PLAYER_SCORE}.")
        ACCOUNT_TWO = account_comparision()
    elif player_guess == "b" and ACCOUNT_ONE[3] < ACCOUNT_TWO[3]:
        PLAYER_SCORE += 1
        print(f"Correct! Your current score is {PLAYER_SCORE}.")
        ACCOUNT_ONE = account_comparision()
    else:
        print(f"Wrong! Your final score is {PLAYER_SCORE}.")
        PLAY_GAME = False


while PLAY_GAME:
    game_loop()

#
# Has a function specifically for the comparison
# if account_one > account_two
# return player_guess == "a"
# else:
# return player_guess == "b"
