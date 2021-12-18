student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

for result in student_scores:
    if student_scores[result] >= 91:
        student_grades[result] = "Outstanding"
    elif student_scores[result] >= 81:
        student_grades[result] = "Exceeds Expectations"
    elif student_scores[result] >= 71:
        student_grades[result] = "Acceptable"
    elif student_scores[result] <= 70:
        student_grades[result] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# Differences in her code:
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"

# I misnamed the iterator in the for loop
