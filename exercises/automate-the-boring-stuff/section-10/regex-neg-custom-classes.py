import re

# Custom classes provide benefit of negative character classes.
# This allows you to search by everything that ISN'T in your
# regex search terms. This is done using a caret ^
# inside the search's brackets. It means "do the opposite."

regex_consonants = re.compile(r"[^aeiouAEIOU]")  # This is basically "find consonants"
# Except not really only consonants, because it also returns spaces and punctuation.

print(
    (
        'The code `regex_consonants = re.compile(r"[^aeiouAEIOU]")` '
        "returns the following: "
    )
    + str(regex_consonants.findall("Robotcop eats baby food."))
)

# Use \W instead of \w because this is negative. We want
# "all the characters that are not vowels and not not words."
regex_consonants = re.compile(r"[^aeiouAEIOU\W]")
print(
    (
        "Because this actually includes spaces and punctuation as well "
        'it might be best to do `regex_consonants = re.compile(r"[^aeiouAEIOU\W"])` '
        "to return:" + str(regex_consonants.findall("Robotcop eats baby food."))
    )
)
