import re

# ? match preceeding group 0 or 1 times
bat_regex = re.compile(r"Bat(wo)?man")
# ? says this group (wo) can appear in the text 0 or 1 times
mo = bat_regex.search("The Adventures of Batman.")
print(mo.group())
mo = bat_regex.search("The Adventures of Batwoman.")
print(mo.group())

# ? allows both Batman and Batwoman to be found in text

mo = bat_regex.search(
    "The Adventures of Batwowowowoman."
)  # ? will not find anything here

phone_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phone_regex.search("My phone number is 415-555-1234. Call me tomorrow.")
print(mo.group())

mo = phone_regex.search("My phone number is 555-1234. Call me tomorrow.")
if mo is True:
    print(mo.group())
else:
    print("Search failed.")

phone_regex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")  # makes area code optional
print(phone_regex.search("My phone number is 415-555-1234"))
print(phone_regex.search("My phone number is 555-1234"))
