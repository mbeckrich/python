range(4)  # is similar to
[0, 1, 2, 3]  # in that
for i in range(4):
    print(i)
# and
for i in [0, 1, 2, 3]:
    print(i)
# produce the same result
# Breakdown:
# assign i to 0, print(i) = 0
# assign i to 1, print (i) = 1
# etc.

range(4)  # is a sequence, 'list-like'
print(range(4))
list(range(4))  # turns sequence into actual list
print(list(range(4)))

# For loops iterate over the values in a list
