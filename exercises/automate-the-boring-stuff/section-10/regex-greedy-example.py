import re

digit_regex = re.compile(r"(\d){3,5}")
print(digit_regex.search("1234567890"))

# By default, regex does greedy matches -- longest possible string that patches a given
# pattern.
# Above is ambiguous, so regex will try to match longest string.


# ? after squiggly bracket asks for non-greedy search, returns shortest possible string
digit_regex = re.compile(r"(\d){3,5}?")
print(digit_regex.search("1234567890"))
