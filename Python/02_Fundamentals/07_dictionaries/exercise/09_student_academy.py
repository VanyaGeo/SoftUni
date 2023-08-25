number_of_pairs = int(input())

student_academy_dict = {}

for number in range(number_of_pairs):
    student = input()
    grade = float(input())

    if student not in student_academy_dict:
        student_academy_dict[student] = []

    student_academy_dict[student].append(grade)

average_grades = {name: sum(grade) / len(grade) for name, grade in student_academy_dict.items()
                  if sum(grade) / len(grade) > 4.50}
for name, average_grade in average_grades.items():
    print(f"{name} -> {average_grade:.2f}")

# for names, grades in student_academy_dict.items():
#     average_grade = sum(grades) / len(grades)
#     if average_grade < 4.50:
#         continue
#
#     print(f"{names} -> {average_grade:.2f}")


# 5
# Amanda
# 3.5
# Amanda
# 4
# Rob
# 5.5
# Christian
# 5
# Robert
# 6
