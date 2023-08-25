course_registered_students = {}

command = input()

while command != "end":
    command_ = command.split(" : ")
    course_name = command_[0]
    student_name = command_[1]

    if course_name not in course_registered_students:
        course_registered_students[course_name] = []

    course_registered_students[course_name].append(student_name)

    command = input()

for course, amount_students in course_registered_students.items():
    print(f"{course}: {len(amount_students)}")

    for student in amount_students:
        print(f"-- {student}")

# Programming 02_Fundamentals : John Smith
# Programming 02_Fundamentals : Linda Johnson
# JS Core : Will Wilson
# Java 03.1_Advanced : Harrison White
# end