# First time this is run, `i = 0`. The `for` statement adds 1 to `i`
# each time loop runs up to but not including 5.

print('My name is')
for i in range(5):
	print('Jimmy Five Times ' + str(i))

# starts at 12, goes up to but does not include 16

print('My name is')
for i in range(12, 16):
	print('Jimmy Five Times ' + str(i))
	
# starts at 0, increases by two (the step value, or final number in range, 
# goes up to but does not include 10)
	
print('My name is')
for i in range(0, 10, 2):
	print('Jimmy Five Times ' + str(i))
	
# Counts backwards from 5 down to but not including -1 at a rate of -1
	
print('My name is')
for i in range(5, -1, -1):
	print('Jimmy Five Times ' + str(i))
