import re

# {} looks for an exact match
haRegex = re.compile(r"(Ha){3}")
print(haRegex.search("He said 'HaHaHa'"))

phone_regex = re.compile(
    r"((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}"
)  # {3} just repeats first section 3x
print(phone_regex.search("My phone numbers are 415-555-1234,555-4242,212-555-0000."))
