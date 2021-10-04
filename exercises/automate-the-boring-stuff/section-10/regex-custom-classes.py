import re

# same as r"(a|e|i|o|u)"
regex_obj_vowels = re.compile(r"[aeiouAEIOU]")

# python also recognizes implied characters,
# as with r"[a-z]" containing all lowercase letters of the alphabet
# r"[a-zA-Z]" would return both lowercase and capital letters.

print(
    "The vowels in the sentence 'Robocop eats baby food.' are "
    + str(regex_obj_vowels.findall("Robocop eats baby food."))
)

regex_obj_double_vowels = re.compile(r"[aeiouAEIOU]{2}")
print(
    (
        "This time, our custom regex search of "
        "`regex_obj_double_vowels = re.compile(r'[aeiouAEIOU]{2}')` looks for two "
        "consecutive vowels. Result: "
    )
    + str(regex_obj_double_vowels.findall("Robocop eats baby food."))
)
