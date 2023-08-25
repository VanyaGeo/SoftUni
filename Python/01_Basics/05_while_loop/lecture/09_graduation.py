student_name = input()

grade_sum = 0
grade_count = 0
fail = 0

while True:
    grade = float(input())
    if grade >= 4:
        grade_count = grade_count + 1
        grade_sum = grade_sum + grade
    if grade < 4:
        fail = fail + 1
        if fail == 2:
            grade_count = grade_count + 1
            print(f"{student_name} has been excluded at {grade_count} grade")
            break

    if grade_count == 12:
        print(f"{student_name} graduated. Average grade: {grade_sum / grade_count:.2f}")
        break
