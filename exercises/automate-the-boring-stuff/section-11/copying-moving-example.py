import shutil

# Can also provide a new name in second location, e.g/
# "/users/mkb/python test/tagcons/15.svg")
shutil.copy("/users/mkb/python test/tagcons/1.svg", "/users/mkb/python test")

# Creates copy of directory in location provided
shutil.copytree("/users/mkb/python test/tagcons", "/users/mkb/python test/backup/")

# Can be used to move file, rather than copy it (so leaving blank for now)
# shutil.move()

# No rename function, so you use .move, keep in same folder, provide new name for file
# shutil.move("spam.txt", "eggs.txt")
