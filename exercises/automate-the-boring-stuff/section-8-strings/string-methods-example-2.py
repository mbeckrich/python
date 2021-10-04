spam = "Hello world!"
print(
    "Evaluations can be done on strings using .islower() and .isupper(). For",
    "example, if spam = 'Hello world!', then spam.islower() will return:",
    spam.islower(),
)

print("String methods can be stacked on each other. For example:")
print("'Hello'.upper() will return:", "Hello".upper())
print("But 'hello'.upper().isupper() will return a Boolean:", "hello".upper().isupper())

print("Many other methods exist to evaluate strings. For example:")
print(".isspace() is used to evaluate whether a string has all whitespace in it.")
print("In the case of 'Hello world!'.isspace(), it returns:", "Hello world!".isspace())
print(".isspace() can target an index in the string. For example:")
print("'Hello world!'[5].isspace will return:", "Hello world!"[5].isspace())

print(
    "Another string method is .istitle(), which checks text for title case. That is, when every word begins with a capital letter. For example: 'This Is Title Case.istitle()' will return",
    "This Is Title Case".istitle(),
)
