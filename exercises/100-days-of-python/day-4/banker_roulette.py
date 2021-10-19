import random

# Determine who pays the bill after a meal

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# e.g. 3 people, len returns 2, get position of name in 2 and print?

randomized_names = random.randint(0, len(names) - 1)
print(f"It looks like {names[randomized_names]} will get the bill.")
