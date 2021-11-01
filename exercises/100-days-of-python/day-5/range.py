for number in range(1, 10):
    print(number)
# prints 1-9
# range(1, 11) for 1-10

for number in range(1, 11, 3):
    print(number)
# prints 1, 4, 7, 10. 3 is the 'step'

total = 0  # accumulator
for number in range(1, 101):
    total += number
print(total)
