# I

import math

people = int(input())
elevator_capacity = int(input())

elevator_courses = math.ceil(people / elevator_capacity)

print(elevator_courses)

# II

# people = int(input())
# elevator_capacity = int(input())
#
# full_course = people // elevator_capacity
# half_course = people % elevator_capacity
# if half_course > 0:
#     half_course = 1
# result = full_course + half_course
#
# print(result)