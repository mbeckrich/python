# ########### Scope ############

from typing import NewType


enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) will not work because it is
# defined w/in the function -- local scope, so
# can only be used within walls of the drink_potion()
# function


# Global scope
# Player health is global, not within another function
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()

# Namespace:
# When you give name to something, you have to be aware of
# where you gave name to it. Where you write line of code
# determines the scope of the variable/function.

# No block scope in python
# A variable created within a function can only be accessed in
# that function. Anything else after a : can be accessed
# eslewhere.

game_level = 3
enemies = ["Skeleton", "Zombie", "Bat"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# Modifying global scope
# use global variable_name
# Difficult to do this, and usually don't want to do this
# Confusing, prone to causing bugs/errors
# instead of below, use `return enemies + 1`

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside ufnction: {enemies}")

# Global constants are ALL_UPPERCASE
# e.g. PI = 3.14159, URL = "", TWITTER = ""
