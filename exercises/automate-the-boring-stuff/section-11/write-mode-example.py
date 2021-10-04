# 'w' and 'append' can be used to write to files
# python will create file if it does not yet exist

import os

hello_file = open("/Users/mkb/python test/readme2.md", "w")
hello_file.write("Hello!")

hello_file = open("/Users/mkb/python test/readme2.md", "a")
hello_file.write("\n\nNew file!")

hello_file = open("/Users/mkb/python test/readme2.md", "a")

hello_file.close()
