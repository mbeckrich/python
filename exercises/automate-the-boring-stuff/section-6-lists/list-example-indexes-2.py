# Lists of lists
# spam = [["cat", "bat"], 10, 20, 30, 40, 50]
# spam[0] This returns ['cat', 'bat'] because this is the first item
# in the list
# spam[0][1] This returns 'bat', because the index finds cat, bat and
# then the second item in the list, bat.
# spam = [["cat", "bat"], 10, 20, 30, 40, 50]
# spam[0][1]
# [["cat", "bat"], 10, 20, 30, 40, 50]
# [0] | ["cat", "bat"]
# [1] | 'bat'

# spam[1][4]
# [["cat", "bat"], 10, 20, 30, 40, 50]
# [1] | [10, 20, 30, 40, 50]
# [4] | 50

spam = ["cat", "bat", "rat", "elephant"]
spam[-1]  # The [-1] index refers to the last item in the list `'elephant`
spam[-2]  # The [-2] index refers to the second to last item in the list

print("The " + spam[-1] + " is afraid of the " + spam[-3] + ".")
