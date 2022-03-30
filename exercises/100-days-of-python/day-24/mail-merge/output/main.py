# for each name in invited_names.txt:
# replace the [name] placeholder witht he actual name
# save the letters in the folder ready to send

names = open("day-24/mail-merge/names/invited_names.txt", mode="r").readlines()

letter = open(
    "day-24/mail-merge/letters/starting_letter.txt", mode="r"
).readlines()
x = []

for replacement in letter:
    for name in names:
        name = name.strip()
        with open(
            f"day-24/mail-merge/output/readytosend/letter_for_{name}.txt",
            mode="a",
        ) as new_letter:
            new_letter.write(replacement.replace("[name]", name))

    # replacement.replace("[name],", f"{name},")
# with open(
#     "day-24/mail-merge/output/readytosend/sample.txt", mode="w"
# ) as new_letter:
#     new_letter.write(x)
