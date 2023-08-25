# line = input().split()
# first_string = line[0]
# second_string = line[1]
# result = 0
#
# if len(first_string) > len(second_string):
#     for char in range(len(second_string)):
#         result += ord(first_string[char]) * ord(second_string[char])
#     for char in range(len(second_string), len(first_string)):
#         result += ord(first_string[char])
#
# elif len(second_string) > len(first_string):
#     for char in range(len(first_string)):
#         result += ord(first_string[char]) * ord(second_string[char])
#     for char in range(len(first_string), len(second_string)):
#         result += ord(second_string[char])
#
# else:
#     for char in range(len(first_string)):
#         result += ord(first_string[char]) * ord(second_string[char])
#
# print(result)

# II

first_string, second_string = input().split()
min_length = min(len(first_string), len(second_string))
result = 0

for char in range(min_length):
    result += ord(first_string[char]) * ord(second_string[char])

for char in range(min_length, len(first_string)):
    result += ord(first_string[char])

for char in range(min_length, len(second_string)):
    result += ord(second_string[char])

print(result)

# George Peter