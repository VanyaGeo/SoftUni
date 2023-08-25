import sys

n_input = int(input())

max_number = -sys.maxsize
number_sum = 0
current_num = 0

for num in range(1, n_input+1):
    current_num = int(input())
    if current_num > max_number:
        max_number = current_num
    number_sum = number_sum + current_num

if number_sum - max_number == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    number_sum -= max_number
    print("No")
    print(f"Diff = {abs(number_sum - max_number)}")
