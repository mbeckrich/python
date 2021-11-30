# Modify jump function
# Use more while loops
# Use reeborg's keyboard
# She did it in 24 lines

# Move forward UNLESS facing wall
# IF facing wall, turn left
# MOVE until no wall on right (if wall on right...)
# THEN turn right
# THEN move
# THEN turn right
# THEN move until wall in front (if wall in front...)
# THEN turn left


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def adjust():
#     turn_right()
#     move()
#     turn_right()
#     while wall_in_front() == False:
#         move()
#     else:
#         turn_left()


# def going_up():
#     while wall_in_front() == False:
#         move()
#     else:
#         turn_left()
#     while wall_on_right():
#         move()
#     else:
#         adjust()


# def jump():
#     while at_goal() == False:
#         going_up()


# jump()

# Her method uses many fewer loops; similar number of
# steps on the site, but maybe easier to read and
# definitely shorter.


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
