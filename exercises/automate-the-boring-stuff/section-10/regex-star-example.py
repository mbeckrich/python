import re

# bat_regex = re.compile(r"Bat(wo)?man") will not find anything in The Adventures of
# Batwowowowoman because it only searches for 0 or 1 wo

bat_regex = re.compile(r"Bat(wo)*man")  # This will
print(bat_regex.search("The Adventures of Batwowowoman"))

bat_regex = re.compile(r"Bat(wo)+man")
if bat_regex is True:
    print(
        bat_regex.search("The Adventures of Batman")
    )  # Will not work, because wo is required to equal at least 1
else:
    print("Need Batwoman!")

# \ means 'literal' character. \+ means the literal + as opposed to the search tool
