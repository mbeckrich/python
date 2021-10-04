import re

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

# | pipes can be used to extend number of options, e.g. re.IGNORECASE | re.DOTALL, etc.
