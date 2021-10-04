import re

regex_names = re.compile(r"Agent \w+")
print(regex_names.findall("Agent Alice gave the secret documents to Agent Bob."))

# Sub = Substitute, replaces what is found by regex with what is inside .sub()

print(
    regex_names.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob.")
)

regex_names = re.compile(r"Agent (\w)\w*")

# Returns the group, not the entire name
print(regex_names.findall("Agent Alice gave the secret documents to Agent Bob."))

# Use a r"" because we want a literal backslash in the string
# \1 says "I want some part of the original matching string," can go beyond \2, \3, etc.
print(
    regex_names.sub(
        r"Agent \1*****", "Agent Alice gave the secret documents to Agent Bob."
    )
)
