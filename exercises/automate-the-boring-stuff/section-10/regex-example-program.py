import pyperclip
import re

regex_phone = re.compile(
    r"""
    (
((\d\d\d) | (\(\d\d\d\)))?
(\s|-|.)
\d\d\d
(\s|-|.)
\d\d\d\d
(((ext(\.)?\s)|x)
(\d{2,5}))?
)""",
    re.VERBOSE,
)

regex_email = re.compile(
    r"""
[a-zA-Z0-9_.+]+ # name part of email
@ # @ symbol
[a-zA-Z0-9_.+]+ # domain name
""",
    re.VERBOSE,
)

text = pyperclip.paste()

phone_extracted = regex_phone.findall(text)
email_extracted = regex_email.findall(text)

phone_all_numbers = []
for phone_number in phone_extracted:
    phone_all_numbers.append(phone_number[0])

results = "\n".join(phone_all_numbers) + "\n" + "\n".join(email_extracted)
pyperclip.copy(results)
