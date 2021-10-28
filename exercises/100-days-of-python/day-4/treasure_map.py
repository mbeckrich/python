# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

position = list(position)
position.reverse()
position0 = int(position[0]) - int(1)
position1 = int(position[1]) - int(1)

map[position0][position1] = "x"
# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# Differences with her code:
# 1) She wrote the below, which avoids having to directly
# convert to a list or use the .reverse() method.c3
# It saves her one line. She does another version closer to mine
# later.
# position = input('Where do you want to put the treasure? ')
# horizontal = int(position[0])
# vertical = int(position[1])
# selected_row = map[vertical - 1]
# selected_row[horizontal - 1] = 'X'
# Her method saves some work but I have a harder time reading it.
# 2) is:
# horizontal = int(position[0])
# vertical = int(position[1])
# map[vertical - 1][horizontal - 1] = "X"
# Using a better variable name like 'horizontal'/'vertical' might
# have made this easier.
