number_of_students = int(input())
average_grade = 0
grades_dict = {}

for student in range(number_of_students):
    name, grade = input().split()
    if name not in grades_dict:
        grades_dict[name] = []
    grades_dict[name].append(float(grade))

for key, value in grades_dict.items():
    average_grade = (sum(grades_dict[key])) / len(grades_dict[key])

    print(f"{key} -> {''.join([str(f'{grade:.2f}') for grade in value])} (avg: {average_grade:.2f})")
