# Much simpler way to identify phone numbers when compared to regex-example-1.py.

import re  # imports regex module

message = "Call me 415-555-1011 tomorrow, or at 415-55-99"

phone_num_regex = re.compile(
    r"\d\d\d-\d\d\d\-\d\d\d\d"
)  # r is used to prevent code treated as escape characters
mo = phone_num_regex.search(message)
print(mo.group())

# findall() can be used instead of search()

phone_num_regex = re.compile(r"\d\d\d-\d\d\d\-\d\d\d\d")
print(phone_num_regex.findall("Call me 415-555-1011 tomorrow, or at 415-555-9999"))

# From findall() vid
# re.compile(r"\d") is same as saying (r"0|1|2|3|4|5|6|7|8|9")
