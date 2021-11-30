# FOLLOW RIGHT WALL IF CAN
# TURN RIGHT IF NOT
# TURN LEFT AS LAST RESORT

# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#         if front_is_clear() and wall_on_right() == False:
#             turn_right()
#     elif wall_in_front() and wall_on_right():
#         turn_left()
#     else:
#         turn_right()

# Differences with her code:
# She uses:
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# She provides three extra 'problem worlds' where her
# original code would not work correctly.
# Mine handled first two, third fails.
# She adds three lines to top of her code:
# while front_is_clear():
#     move()
# turn_left()
