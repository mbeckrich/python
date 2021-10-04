import re

# Common regex character classes
# \d -- digits from 0-9
# \D any character that is NOT a numeric digit from 0-9 i.e. anything but \d
# \w any letter, numeric digit, or underscore character (matches "word" characters)
# Doesn't include punctuation/spaces
# \W any character that is NOT \w
# \s any space, tab, or newline character (matches "space" characters)
# \S any character that is NOT \s


# Find every pattern some number followed by some word
lyrics = """12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree.
"""

# Looks for one or more digit (e.g. 12, one space, one or more words)
xmas_regex = re.compile(r"\d+\s\w+")
print(xmas_regex.findall(lyrics))

# lyrics is formated as 'n + " " + w, so once it gets to second space
# it will stop search e.g "12 drummers drumming" does not fit the pattern
# only "12 drummers" (n + " " + w)
