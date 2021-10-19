import random

print("Heads or tails generator. Flipping a coin now...")
random_integer = random.randint(0, 1)
heads = random_integer
if heads == 0:
    print("Heads.")
else:
    print("Tails.")
