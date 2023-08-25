number_pairs = int(input())
previous_sum_pair_numbers = 0
current_sum_pair_numbers = 0
first_number = 0
second_number = 0
max_diff = 0

for i in range(1, number_pairs + 1):
    if i == 1:
        first_number = int(input())
        second_number = int(input())
        previous_sum_pair_numbers = first_number + second_number
    if i != 1:
        number_1 = int(input())
        number_2 = int(input())
        current_sum_pair_numbers = number_1 + number_2
    max_diff = abs(current_sum_pair_numbers - previous_sum_pair_numbers)
if max_diff == 0 or number_pairs == 1:
    print(f"Yes, value={previous_sum_pair_numbers}")
# elif max_diff != 0:
else:
    print(f"No, maxdiff={max_diff}")

