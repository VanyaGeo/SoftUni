integer_string = input().split(", ") # instead of line 1 and line 6, use comment on line 6
beggars = int(input())
final_list = []
counter_of_index = 0
temporary_sum = 0
sums_list_as_digits = [] # integer_string = [int(n) for n in input().split(", ")]

for index in range(len(integer_string)):
    sums_list_as_digits.append(int(integer_string[index]))

while counter_of_index < beggars:
    for element in range(counter_of_index, len(sums_list_as_digits), beggars):
        temporary_sum += sums_list_as_digits[element]

    final_list.append(temporary_sum)
    temporary_sum = 0
    counter_of_index += 1

print(final_list)

