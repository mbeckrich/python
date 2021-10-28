import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]

print("This is a game of rock, paper, scissors.")
player_choice = int(
    input("Please type 0 for rock, 1 for paper, or 2 for scissors. \n")
)

if player_choice >= 3 or player_choice < 0:
    print("You have entered an invalid number.")

else:
    print(f"You chose: \n\n{choices[player_choice]}")

    computer_choice = random.randint(0, 2)

    print(f"The computer chose: \n\n{choices[computer_choice]}")

    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose!")
    elif player_choice > computer_choice:
        print("You win!")
    elif computer_choice > player_choice:
        print("You lose!")
    elif computer_choice == player_choice:
        print("You have tied the computer.")
