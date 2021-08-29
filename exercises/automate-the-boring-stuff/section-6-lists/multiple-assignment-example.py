cat = ["fat", "orange", "loud"]
size, color, disposition = cat
print(size)
print(color)
print(disposition)

# line 2 is multiple assignment in action, prevents
# having to write size = cat[0] and so on.
# matches order of variables to index (e.g. cat[0] is
# size)

size, color, disposition = "skinny", "black", "quiet"
print(size, color, disposition)

# assigns multiple values to variables at one time
