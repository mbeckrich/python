# This runs a loop until spam > 5. At the end
# of a `while` block, execution jumps back to
# beginning of the statement to recheck it. If
# condition is still true, will rerun the block.

spam = 0
while spam < 5:
    print("Hello world!")
    spam = spam + 1
