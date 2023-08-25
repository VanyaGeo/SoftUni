# print(15 % 10) = 5
# print(15//10) = 1
# print(15/10) = 1.5

number = int(input())

for i in range(1, number+1):
    digits = i
    sum_of_digits = digits % 10 + digits // 10
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{digits} -> True")
    else:
        print(f"{digits} -> False")

