import math

students = int(input())
lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
student_attendance = 0

for class_attend in range(1, students + 1):
    attendance = int(input())
    total_bonus = math.ceil(attendance / lectures * (5 + additional_bonus))
    if attendance > student_attendance:
        max_bonus = total_bonus
        student_attendance = attendance

print(f"""Max Bonus: {max_bonus}. 
The student has attended {student_attendance} lectures.""")


