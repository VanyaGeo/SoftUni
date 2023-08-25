poor_grades_number = int(input())
current_poor_grades = 0
problems = 0
total_grades = 0
last_name = ""

while True:

    problem_name = input()

    if problem_name == "Enough":
        average_score = total_grades / problems
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {problems}")
        print(f"Last problem: {last_name}")
        break

    grade = int(input())

    total_grades = total_grades + grade
    problems = problems + 1
    last_name = problem_name

    if grade <= 4:
        current_poor_grades = current_poor_grades + 1
        if current_poor_grades == poor_grades_number:
            print(f"You need a break, {poor_grades_number} poor grades.")
            break
