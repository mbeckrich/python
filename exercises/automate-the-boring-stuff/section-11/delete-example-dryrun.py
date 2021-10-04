# A dryrun means to comment out big actions like deletion
# Below prevents deletion but lists the files that would be deleted
# In this case, any file with our typoed extension would be listed,
# rather than deleted.

import os

for filename in os.listdir():
    if filename.endswith(".rxt"):
        # os.unlink(filename)
        print(filename)

# Once ready, uncomment os.unlink() and comment print()

# Use pip to install send2trash, which will move files to trash instead of
# permanently deleted. This is much safer. Would then use import send2trash
# and use send2trash() function
