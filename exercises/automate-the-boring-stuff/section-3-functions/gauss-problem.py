# range goes up but not not including number in range call,
# so 101 instead of 100.

total = 0
for num in range(101):
		total = total + num 
print(total)

# this solves the same problem, but requires additional code

print('My name is')
i = 0
while i < 5:
	print("Jimmy Five Times " + str(i))
	i = i + 1
	
