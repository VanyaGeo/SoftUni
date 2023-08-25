def gather_credits(credits_number, *args):
    gathered_credits = 0
    needed_credits = int(credits_number)
    enrolled_courses = []
    result = ""

    for course in args:
        course_name, course_credits = course
        if gathered_credits >= needed_credits:
            break
        else:
            if course_name not in enrolled_courses:
                enrolled_courses.append(course_name)
                gathered_credits += course_credits

    if gathered_credits >= needed_credits:
        sorted_courses = sorted(enrolled_courses, key=lambda x: x)
        result += f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted_courses)}"
    else:
        difference = needed_credits - gathered_credits
        result += f"You need to enroll in more courses! You have to gather {difference} credits more."

    return result




print(gather_credits(
    80,
    ("Basics", 27),
))
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
