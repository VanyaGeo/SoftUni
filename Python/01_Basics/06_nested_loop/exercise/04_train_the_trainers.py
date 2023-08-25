jury = int(input())
sum_grades = 0
grades_amount = 0

course_name = input()
while course_name != "Finish":
    current_course_grades = 0

    for i in range(jury):
        grade = float(input())
        grades_amount += 1
        current_course_grades += grade
        sum_grades += grade

    average_sum_grades = current_course_grades / jury
    print(f"{course_name} - {average_sum_grades:.2f}.")

    course_name = input()

if course_name == "Finish":
    average = sum_grades / grades_amount
    print(f"Student's final assessment is {average:.2f}.")