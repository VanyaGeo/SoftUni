n_lines = int(input())

longest_intersection = set()

for i in range(n_lines):
    first_info, second_info = [[int(num) for num in x.split(",")] for x in input().split("-")]
    first_range = set(range(first_info[0], first_info[1] + 1))
    second_range = set(range(second_info[0], second_info[1] + 1))

    intersection = first_range.intersection(second_range)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] "
      f"with length {len(longest_intersection)}")