# Hint 4: Create a deal_card() function

import random


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Hint 6: Create a function called calculate_score that takes list as input and returns score

# Hint 7: Check for blackjack: Ace + 10

# Hint 8: Check for 11, remove and replace with 1 if > 21


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# Hint 13: Use function to compare user and computer score
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, computer has Blackjack."
    elif user_score == 0:
        return "You win with Blackjack!"
    elif user_score > 21:
        return "Bust! You lose."
    elif computer_score > 21:
        return "Bust! Computer loses."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


# Hint 5: Deal user and computer two cards each using deal_card()
def play_game():

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        # use append instead of += to avoid error
        # += is short for (extend), which requires a list to be added to a list

    while not is_game_over:

        # Hint 9: Call calcuate_score(), stop game if blackjack
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards} and score: {user_score}.")
        print(f"    Computer's first card: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        # Hint 10: If game is not over, ask user if they want to draw another card.
        # If no, game ends.
        else:
            user_should_deal = input(
                "Type 'y' to get another card or type 'n' to pass. "
            )
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Hint 12: Once user finishes, computer draws while score < 17
    # Exclude 0
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}.")
    print(
        f"    Computer's final hand: {computer_cards}, final score:"
        f" {computer_score}."
    )

    print(compare(user_score, computer_score))


# Hint 14: Ask user if they want to restart game
while (
    input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y"
):
    play_game()


# Takeaways:
# Can stand to put way more stuff into functions.
# It makes her code much simpler.
