import re

regex_phone = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
print(regex_phone)

# findall() allows search of all regex matches in string. search() returns match
# objects, findall() returns list of strings

resume = """ Test test cell: 508-555-5555 home: 123-123-1234
Blah blah blah
Hello!
"""

print(regex_phone.findall(resume))  # Shows all phone numbers in resume variable
print(regex_phone.search(resume))  # Returns only first phone number in resume variable

# findall() will return regex matches based on 0 or 1 groups in search

regex_phone = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")  # two groups
print(regex_phone)
print(regex_phone.findall(resume))
# because >= 2 groups, returns list of tuples comprised of strings

# could place entire search in parentheses to create 3rd group
regex_phone = re.compile(r"((\d\d\d)-(\d\d\d-\d\d\d\d))")
print(regex_phone)
print(regex_phone.findall(resume))
# returns tuple containing all three groups

print(
    str(regex_phone.findall(resume)[0:1])
    + "is the first number's three groups in the resume."
)
print(
    str(regex_phone.findall(resume)[1:2])
    + "is the second number's three groups in the resume."
)
