# sum() function adds items in a list, can't be used in exercise

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# print(sum(student_heights)) adds list, can replicate with:

all_heights = 0
for height in student_heights:
    all_heights += height
print(all_heights)

# average_height = round(all_heights / (n + 1))

all_students = 0
for student in student_heights:
    all_students += 1

average_height = round(all_heights / all_students)
print(average_height)
