elements = [element.lower() for element in input().split()]
my_dict = {}

for el in elements:
    key = el
    if key not in my_dict.keys():
        my_dict[key] = 1
    else:
        my_dict[key] += 1

for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

# II
# elements = input().lower().split()
# default = 0
#
# occurrences = dict.fromkeys(elements, default)
# for keys in elements:
#     occurrences[keys] += 1
#
# for key, value in occurrences.items():
#     if value % 2 != 0:
#         print(key, end=" ")


# Java C# PHP PHP JAVA C java