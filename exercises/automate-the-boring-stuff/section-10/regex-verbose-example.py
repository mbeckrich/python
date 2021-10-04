import re

# Verbose format helps clarify regex searches, can use multi string. Can place
# comments inside

re.compile(
    r"""
\d\d\d #area code
- # first dash
\d\d\d #first three digits
- #second dash
\d\d\d\d #last four digits""",
    re.verbose,
)

re.compile(
    r"""
(\d\d\d)    #area code (without parens, no dash)
-           # first dash
(\(\d\d\d)) # Area code with parens and no dash
\d\d\d      # first three digits
-           #second dash
\d\d\d\d    #last four digits
\sx\d{2,4}  #extension""",
    re.verbose,
)
