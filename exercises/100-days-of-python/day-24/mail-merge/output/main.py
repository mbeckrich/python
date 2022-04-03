names = open("day-24/mail-merge/names/invited_names.txt", mode="r").readlines()

letter = open(
    "day-24/mail-merge/letters/starting_letter.txt", mode="r"
).readlines()
# She uses .read()

for replacement in letter:
    for name in names:
        name = name.strip()
        with open(
            f"day-24/mail-merge/output/readytosend/letter_for_{name}.txt",
            mode="a",
        ) as new_letter:
            new_letter.write(replacement.replace("[name]", name))

# Her code
# with open() as names_file:
#     names = names_file.readlines()

# with open() as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.srtip()
#         new_letter = letter_contents.replace(var, stripped_name)
#         with open(mode="w") as completed_letter:
#             completed_letter.write(new_letter)
