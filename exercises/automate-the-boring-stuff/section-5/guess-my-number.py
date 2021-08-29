# This is a guess the number game.
import random

print("Hi, what is your name?")
name = input()

print("Well, " + name + ", I am thinking of a number between one and 20.")
secretNumber = random.randint(1, 20)

print("DEBUG: Secret number is " + str(secretNumber))
# This is temporary code that allows us to test the program by giving us
# the secret number ahead of time.

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # This condition is for the correct guess.

if guess == secretNumber:
    print(
        "Good job, "
        + name
        + "! You guessed my number in "
        + str(guessesTaken)
        + " guesses."
    )
else:
    print("Nope, the number I was thinking of was " + str(secretNumber) + ".")
