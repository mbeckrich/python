# import random
# import pandas

# keyword method:
# name_for_new_list = [new_item for current_item in current_list]
# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# # With strings
# name = "Marshall"
# new_list = [letter for letter in name]
# print(new_list)

# # Conditional lists
# names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
# # short names = [new_item for current_item in current_list if test_passes]
# short_names = [name.upper() for name in names if len(name) >= 5]
# print(short_names)

# with open("file1.txt") as file1:
#     file1 = file1.readlines()


# with open("file2.txt") as file2:
#     file2 = file2.readlines()


# result = [int(num) for num in file1 if num in file2]

# # Write your code above 👆

# print(result)

# dict comprehension
# new_dict = {new_key:new_value for item in list/iterable}
# or new_dict = new_key:new_value for (key,value) in dict.items()}
# or new_dict = {new_key:new_value for (key,value) in dict.items() if...}

# names = ["ira", "lizzy", "marshall", "cassie", "cipher", "tenley"]
# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)

# passed_students = {
#     student: score
#     for (student, score) in dict.items(student_scores)
#     if score >= 60
# }
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# sentence = sentence.split()

# print(sentence)
# result = {words: len(words) for words in sentence}
# # Write your code below:


# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆

# weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}

# # Write your code 👇 below:

# print(weather_f)

# iterrows
# for (index, row) in dataframe.iterrows():
#     print(index) or print(row)
