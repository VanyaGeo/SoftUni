command = input()

courses = {}

while ":" in command:
    name, student_id, course = command.split(":")
    if course not in courses:
        courses[course] = {name: student_id}
    else:
        courses[course][name] = student_id
    command = input()

course_name = command.replace("_", " ")
# course_name = " ".join(command.split("_"))

students = courses[course_name]

for name, student_id in students.items():
    print(f"{name} - {student_id}")
