# with open("day-24/high_score.txt") as file:
#     contents = file.read()
#     print(contents)
# mode = w, write | mode = a, append | mode = r, read

with open("day-24/new_file.txt", mode="w") as file:
    file.write("New text.")
