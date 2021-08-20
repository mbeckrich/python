# This skips `spam is 3` because when `if spam == 3`
# evaluates to True, `if spam == 3: continue` is executed
# and loop begins again. `continue` statement causes execution
# to immediately jump back to the start of the loop
# and recheck the condition.

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print("spam is " + str(spam))
