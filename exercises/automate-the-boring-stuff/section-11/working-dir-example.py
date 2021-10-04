import os

# shows the working directory for python, assumes that file being worked on is there
# unless told otherwise
os.getcwd

# Used to change working directory
os.chdir
# e.g. os.chdir(./.config)

# Relative file path is based on working directory. e.g. 'spam.png' is assumed to be in
# the working directory. Relative file path can also be used with some direction. e.g.,
# 'folder1/folder2/spam.png' is assumed to be in the working directory.
# Absolute path is the exact path to the file/folder

# . is current directory
# .. is parent folder

# os.path.abspath() gives the absolute path of your file, can be used from
# a relative path

# os.path.isabs() programatically determines if absolute path

# os.path.relpath() gives relative path between two given paths, e.g.,
# os.path.relpath('./.config/fish', 'fish')

# os.path.dirname() gets folder names to file, stops at last slash

# os.path.basename() gets file name, starts at last slash

# os.path.exists() will return True or False based on whether location exists

# os.path.isfile() returns whether location is file

# os.path.isdir() returns whether location is folder

# os.makedirs() can be used to create folders
