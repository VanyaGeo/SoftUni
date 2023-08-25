first_num = int(input())
second_num = int(input())

for num in range(first_num, second_num + 1):
    current_num = str(num)
    even_sum = 0
    odd_sum = 0

    for i in range(0, len(current_num)):
        digit = int(current_num[i])
        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(current_num, end=" ")

