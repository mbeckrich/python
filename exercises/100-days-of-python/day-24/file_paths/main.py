# Absolute path
with open("/Users/mkb/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
    
# Working dir:
# /Users/mkb/repositories/mbeckrich/python/exercises/100-days-of-python/day-24

with open("../../../../../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
