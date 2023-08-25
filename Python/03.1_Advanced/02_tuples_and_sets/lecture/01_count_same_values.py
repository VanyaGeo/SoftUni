# I
numbers_sequence = [float(x) for x in input().split()]
occurrences = {}

for num in numbers_sequence:
    occurrences[num] = numbers_sequence.count(num)


for key, value in occurrences.items():
    print(f"{key} - {value} times")

# II
#
# numbers_sequence = tuple([float(x) for x in input().split()])
# occurrences = {}
#
# for num in numbers_sequence:
#     occurrences[num] = numbers_sequence.count(num)
#
#
# for key, value in occurrences.items():
#     print(f"{key} - {value} times")