# Creates userdefined function


def hello():
    print("Howdy!")  # body of the function
    print("Howdy!!!")  # body of the function
    print("Hello there.")  # body of the function


hello()
hello()
hello()


def hello(name):  # `name` is a parameter and variable
    print("Hello " + name)  # body of the function


hello("Alice")  # "Alice" is an argument that is assigned to the name parameter
hello("Bob")

# In terminal python, this prints 'Hello has 5 letters in it.'
# 'Hello has ' + str(len('hello')) + ' letters in it.'
# 'Hello has ' + str(5) + ' letters in it.'
# 'Hello has ' + '5' + ' letters in it.'
# 'Hello has 5 letters in it.'
