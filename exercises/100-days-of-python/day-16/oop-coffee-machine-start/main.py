from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MACHINE_ON = True
REMAINING_SUPPLIES = CoffeeMaker()
DRINK = Menu()
PAYMENT = MoneyMachine()

while MACHINE_ON:
    user_order = DRINK.find_drink(
        input(f"What to drink: {DRINK.get_items()}: ")
    )
    if user_order is None:
        print(REMAINING_SUPPLIES.report())
        print(PAYMENT.report())
    elif REMAINING_SUPPLIES.is_resource_sufficient(user_order):
        if PAYMENT.make_payment(user_order.cost):
            REMAINING_SUPPLIES.make_coffee(user_order)
    else:
        MACHINE_ON = False

# Differences in her code:
# By separating drink choice into its own variable
# `choice` she is able to better handle report/off
# exit of the program. Couldn't get this to work how
# I did it.
# turns lines 17 and 18 into one line with `and`
