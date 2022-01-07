from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card():
    the_draw = {}
    the_draw["draw"] = random.choice(cards)
    return [the_draw["draw"]]


your_hand = []
dealer_hand = []
play_game = True

while play_game:
    print(logo)
    confirm_start = input(
        "Do you want to play a game of Blackjack? Type 'yes' or 'no.'"
    ).lower()
    if confirm_start == "yes":
        for n in range(2):
            your_hand += card()
            your_score = sum(your_hand)
            dealer_hand += card()
            dealer_score = sum(dealer_hand)
        print(f"Your cards are {your_hand} and your score is: {your_score}.")
        print(f"The dealer's visible card and score is: {dealer_hand[0]}.")
        if your_score == 21:
            if dealer_score == 21:
                print("Dealer Blackjack! You lose.")
            print("Blackjack! Congrats, you won.")
            exit()
    if confirm_start == "no":
        exit()

    confirm_again = input("Would you like to draw again?").lower()
    while confirm_again == "yes":
        for n in range(1):
            your_hand += card()
            your_score = sum(your_hand)
        if your_score == 21:
            print("Blackjack! Congrats, you won.")
            exit()
        if your_score > 21:
            print(
                f"Your cards are {your_hand} and your score is now:"
                f" {your_score}. Bust!"
            )
            exit()
        print(
            f"Your cards are now {your_hand}, making your score: {your_score}."
        )
        confirm_again = input("Would you like to draw again?").lower()

    if dealer_score == 21:
        print(f"Blackjack! The dealer wins with a hand of {dealer_hand}.")
        exit()
    if dealer_score > 21:
        print(
            f"The dealer's cards are {dealer_hand} and their score is"
            f" now: {dealer_score}. Bust!"
        )
        exit()
    print(
        f"The dealer's hand is {dealer_hand} and their score is:"
        f" {dealer_score}."
    )

    while dealer_score <= 16:
        print(
            f"The dealer remains under 16 with a hand of {dealer_hand} and"
            " must draw again."
        )
        for n in range(1):
            dealer_hand += card()
            dealer_score = sum(dealer_hand)
        if dealer_score > 21:
            print(
                f"The dealer's cards are {dealer_hand} and their score is"
                f" now: {dealer_score}. Bust!"
            )
            exit()
        if dealer_score == 21:
            print(f"Blackjack! The dealer wins with a hand of {dealer_hand}.")
            exit()
    print(
        f"The dealer exceeds 16 with a hand of {dealer_hand} and stops"
        f" drawing with a score of: {dealer_score}."
    )

    if your_score > dealer_score:
        print("You win!")
        exit()
    if your_score == 21:
        print("You win!")
        exit()
    if your_score > dealer_score:
        print("You win!")
        exit()
    if your_score < dealer_score:
        print("You lose!")
        exit()

    else:
        play_game = False
