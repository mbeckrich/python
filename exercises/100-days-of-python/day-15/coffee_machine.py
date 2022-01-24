from art import prices

INVENTORY = {
    "espresso": {"water": 50, "coffee": 18},
    "latte": {"water": 200, "coffee": 24, "milk": 150},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100},
    "price": {"espresso": 1.50, "latte": 2.50, "cappuccino": 3.00},
}

COINS = {"quarter": 0.25, "dime": 0.10, "nickel": 0.05, "penny": 0.01}

DRINK_INGREDIENTS = {"water": 300, "coffee": 100, "milk": 200, "money": 0}

MACHINE_ON = True


def turn_off():
    exit()


def ingredients_left(ingredient_used):
    """Tracks the resources needed by machine for a drink,
    then compares them the machine's ingredients.
    """
    global MACHINE_ON
    DRINK_INGREDIENTS["money"] += INVENTORY["price"][drink_choice]
    for v in ingredient_used:
        DRINK_INGREDIENTS[v] -= ingredient_used[v]
    if DRINK_INGREDIENTS[v] < 0:
        print("A required ingredient is out of stock.")
        turn_off()


def drink_payment(quarters, dimes, nickels, pennies):
    """Takes number of coins and multiplies them by dict value."""
    payment = sum(
        (
            quarters * COINS["quarter"],
            dimes * COINS["dime"],
            nickels * COINS["nickel"],
            pennies * COINS["penny"],
        )
    )
    return payment


def transaction_check(drink_cost):
    global MACHINE_ON
    if drink_cost > INVENTORY["price"][drink_choice]:
        change_due = drink_cost - INVENTORY["price"][drink_choice]
        DRINK_INGREDIENTS["money"] -= change_due
        print(f"Your change is: ${change_due:.2f}.")
    if drink_cost < INVENTORY["price"][drink_choice]:
        print("Sorry, you provided less than the cost of the drink.")
        turn_off()


def report():
    print(
        f"water: {DRINK_INGREDIENTS['water']}ml\n",
        f"coffee: {DRINK_INGREDIENTS['coffee']}g\n",
        f"milk: {DRINK_INGREDIENTS['milk']}ml\n",
        f"${DRINK_INGREDIENTS['money']:.2f}",
    )


while MACHINE_ON:

    print(prices[0], prices[1], prices[2])

    drink_choice = input(
        "Hi! Would you like an espresso, latte, or cappuccino?\n"
    ).lower()

    if drink_choice == "report":
        report()
    elif drink_choice == "off":
        turn_off()
    else:

        ingredients_left(INVENTORY[drink_choice])

        print(
            "Please enter the number of coins you will use as digits."
            " Accepted: quarters, nickels, dimes, and pennies.\n"
        )

        drink_cost = drink_payment(
            quarters=int(input("How many quarters?\n")),
            dimes=int(input("How many dimes?\n")),
            nickels=int(input("How many nickels?\n")),
            pennies=int(input("How many pennies?\n")),
        )

        transaction_check(drink_cost)

# Differences in her code:
# while loop:
# choice = input()
# if choice == "off"
#   is_on = False
# elif choice == "report"
