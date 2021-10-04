# Writing code that changes all files and folders in directory

import os
import shutil

# Iterates over folder names, subfolders, files
for folder_name, subfolders, filenames in os.walk("/users/mkb/python test"):
    print("The folder is " + folder_name)
    print("The subfolders in " + folder_name + " are: " + str(subfolders))
    print("The filenames in " + folder_name + " are: " + str(filenames))
    print()

    # for subfolder in subfolders:
    #     if "spam" in subfolder:
    #         # os.rmdir(subfolder)
    # print("rmdir on " + subfolder)

    # for file in filenames:
    #     if file.endswith(".py"):
    #         shutil.copy(os.join(folder_name, file), file + ".backup")
