# Strings are immutable, so cannot be changed. Using slices
# on a string can be a workaround.

name = "Zophie a cat"
newName = name[0:7] + "the" + name[8:12]  # This removes 'a' and replaces with 'the'


print(newName)
