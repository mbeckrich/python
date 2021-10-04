# Only lets you read file, can't write to it

hello_file = open("/users/mkb/python test/readme.md")

content = hello_file.read()
print(content)

hello_file.close()

# readlines() will return a list of strings

hello_file = open("/users/mkb/python test/readme.md")
content = hello_file.readlines()
print(content)

hello_file.close()
