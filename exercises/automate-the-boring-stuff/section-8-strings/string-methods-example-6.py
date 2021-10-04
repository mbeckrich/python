print(
    "The .strip(), lstrip(), rstrip() string methods can be used to remove characters from a string. For example,\n `spam = 'hello'.rjust(10)` \n spam \n spam = spam.rstrip()`\n will return:",
)
spam = "Hello".rjust(10)
print(spam)
spam = "Hello".strip()
print(spam)

print(
    ".strip() can be passed specific characters to remove. Such as in the case of 'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'):"
)
print("SpamSpamBaconSpamEggsSpamSpam".strip("ampS"))
