import copy

spam = ["A", "B", "C", "D"]
cheese = copy.deepcopy(spam)
# This copies the spam list and creates a new list with
# the same values, but diff reference point

cheese[1] = 42
print(cheese)  # has different reference point for list
print(spam)
