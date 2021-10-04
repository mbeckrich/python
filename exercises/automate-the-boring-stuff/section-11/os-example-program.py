import os

total_size = 0

for filename in os.listdir("/Users/mkb/python test/tagcons"):
    if not os.path.isfile(os.path.join("/Users/mkb/python test/tagcons", filename)):
        continue
    total_size = total_size + os.path.getsize(
        os.path.join("/Users/mkb/python test/tagcons", filename)
    )

# Returns size of all files in location

print(total_size)
