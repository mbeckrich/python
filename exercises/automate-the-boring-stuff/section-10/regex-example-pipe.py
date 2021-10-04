import re

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
print(phone_num_regex.search("My phone number is 415-555-4242"))

mo = phone_num_regex.search("My phone number is 415-555-4242")
print(mo.group())

phone_num_regex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phone_num_regex.search("My phone number is 415-555-4242")
print(
    mo.group(1)
)  # Parentheses in compile act as groups, each pair moves up one (1, 2, 3, etc.)
print(mo.group(2))

# To find parentheses in text, need to escape parentheses with a backlash
phone_num_regex = re.compile(r"\(\d\d\d\) \d\d\d-\d\d\d\d")
mo = phone_num_regex.search("My phone number is (415) 555-4242")
print(mo.group())

# Pipes

bat_regex = re.compile(
    r"Bat(man|mobile|copter|bat)"
)  # Searches for 'Bat' and then any of these possible endings
mo = bat_regex.search("Batmobile lost a wheel.")
print(mo.group())
print(mo.group(1))  # Shows the specific term that was found in the search
