from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def your_cards(n):
    your_draw = {}
    your_draw["draw"] = [random.randint(2, 11) for x in range(n)]
    return your_draw["draw"]


def dealer_cards(n):
    dealer_draw = {}
    dealer_draw["draw"] = [random.randint(2, 11) for x in range(n)]
    return dealer_draw["draw"]


your_hand = []
dealer_hand = []
game_start = True
win_con = 21

while game_start:
    game = input(
        "Do you want to play a game of Blackjack? Type 'yes' or 'no.' "
    )
    if game == "yes":
        print(logo)
        your_hand += your_cards(2)
        your_score = sum(your_hand)
        if 11 in your_hand and your_score > 21:
            your_hand.remove(11)
            your_hand.append(1)
        print(
            f"Your cards are: {your_hand}. Your current score is:"
            f" {your_score}."
        )
        dealer_hand += dealer_cards(2)
        dealer_score = sum(dealer_hand)
        # dealer cannot pick 11 vs 1, must take 11
        # if 11 in dealer_hand and dealer_score > 21:
        #     dealer_hand.remove(11)
        #     your_hand.append(1)
        print(
            f"The dealer drew {dealer_hand[0]} and one hidden card. The"
            f" dealer's known score is {dealer_hand[0]}."
        )
        if your_score == 21:
            print(f"A natural with a score of {your_score}.")
        else:
            draw_again = True
            while draw_again:
                draw = input(
                    "Would you like to draw again? Type 'yes' to get another"
                    " card or 'no' to stand. "
                ).lower()
                if draw == "yes":
                    your_hand += your_cards(1)
                    print(
                        f"Your cards are now: {your_hand} and your score is:"
                        f" {sum(your_hand)}."
                    )
                    if sum(your_hand) == 21:
                        print("Blackjack!")
                        draw_again = False
                        print("You win!")
                    game_start = False
                    if sum(your_hand) > 21:
                        print(f"Your score is {sum(your_hand)}. You lose.")
                        draw_again = False

                if draw == "no":
                    print(
                        "The dealer reveals their face down card:"
                        f" {dealer_hand[1]}. Their full hand is"
                        f" {dealer_hand} and their score is"
                        f" {sum(dealer_hand)}."
                    )
                    while sum(dealer_hand) <= 16:
                        dealer_hand += dealer_cards(1)
                        print(
                            "The dealer must draw again. Their hand is"
                            f" {dealer_hand} and their score is now"
                            f" {sum(dealer_hand)}."
                        )
                    if sum(dealer_hand) >= 17:
                        if sum(dealer_hand) == 21:
                            print(
                                "The dealer wins with a score of"
                                f" {sum(dealer_hand)}."
                            )
                            draw_again = False
                        if sum(dealer_hand) < 22:
                            print(
                                "The dealer must stand. Their score is"
                                f" {sum(dealer_hand)}."
                            )
                        if sum(dealer_hand) > sum(your_hand):
                            print(
                                "The dealer's score of"
                                f" {sum(dealer_hand)} beats your score of"
                                f" {sum(your_hand)}"
                            )
                            draw_again = False
                        if sum(dealer_hand) < sum(your_hand):
                            print("Blackjack! You win")
                            draw_again = False
                        if sum(dealer_hand) > 21:
                            print(
                                "The dealer goes bust with cards"
                                f" {dealer_hand} and score {sum(dealer_hand)}."
                            )
                            draw_again = False
            game_start = False
