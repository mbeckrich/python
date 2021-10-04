import re

haRegex = re.compile(r"(Ha){3,5}")  # min/max number of repetitions
print(haRegex.search("He said 'HaHaHaHa'"))

# If you use line 3 and line 4 has >5 Ha, will only return max number of Ha (5)

haRegex = re.compile(r"(Ha){3,5}")  # min/max number of repetitions
print(haRegex.search("He said 'HaHaHaHaHaHaHaHa'"))

haRegex = re.compile(r"(Ha){3,}")
# As w/ slices, can leave off first/second number e.g.
# {3,} is unbounded max number
print(haRegex.search("He said 'HaHaHaHaHaHaHaHa'"))
