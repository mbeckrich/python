import re

# Caret can be used to say that search find result at beginning of the string
# or else it does not count.

begins_with_Hello_regex = re.compile(r"^Hello")
print(begins_with_Hello_regex.search("Hello there!"))
print(begins_with_Hello_regex.search("He said 'Hello there!'"))  # Will return None

ends_with_world_regex = re.compile(r"world!$")
print(ends_with_world_regex.search("Hello world!"))
print(ends_with_world_regex.search("Hello world! Bye!"))  # Will return None

# ^both$ means regex must find everything in search

all_digits_regex = re.compile(r"^\d+$")
print(all_digits_regex.search("3293094340835058023823"))  # Will return entire string
print(all_digits_regex.search("32930943408350x58023823"))  # Will return None because
# non-digit is inside and ^$ requires entire string to match.

# '.' means any character but newline

at_regex = re.compile(r".at")  # Will find anything that contains [character]at
print(at_regex.findall("The cat in the hat sat on the flat mat"))

at_regex = re.compile(r".{1,2}at")
print(at_regex.findall("The cat in the hat sat on the flat mat"))  # includes whitespace
# characters in result. Anything except the newline character.

# .* means anything/any pattern

print(
    "This: \n"
    '"```First Name: Marshall Last Name: Beckrich".find(":") \n'
    '"First Name: Marshall Last Name: Beckrich".find(":") + 2 \n'
    '"First Name: Marshall Last Name: Beckrich"[12:]``` \n'
    "is a very complicated way to begin saying something better expressed with regex."
)

# Returns one tuple for each group. Look for "First Name: ", find whatever comes after that
# Then looks for "Last Name: " and whatever comes after that.
# .* is greedy
# .*? is non-greedy
name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
print(name_regex.findall("First Name: Marshall Last Name: Beckrich"))

# non-greedy search returns results only inside the <>
serve = "<To serve humans> for dinner.>"
non_greedy_regex = re.compile(r"<(.*?)>")
print(non_greedy_regex.findall(serve))

# greedy search returns everything
serve = "<To serve humans> for dinner.>"
greedy_regex = re.compile(r"<(.*)>")
print(greedy_regex.findall(serve))

# Only returns first line, because . does not search beyond \n
prime = "Serve the public trust.\n Protect the innocent.\n Uphold the law."
dot_star = re.compile(r".*")
print(dot_star.search(prime))

# This says . means everything, including new lines.
prime = "Serve the public trust.\n Protect the innocent.\n Uphold the law."
dot_star = re.compile(r".*", re.DOTALL)
print(dot_star.search(prime))

# Only returns lowercase letters
regex_vowel = re.compile(r"[aeiou]")
print(
    regex_vowel.findall(
        "Al, why does your programming book talk about RoboCop so much?"
    )
)

# re.I ignores case in search
regex_vowel = re.compile(r"[aeiou]", re.I)
print(
    regex_vowel.findall(
        "Al, why does your programming book talk about RoboCop so much?"
    )
)
