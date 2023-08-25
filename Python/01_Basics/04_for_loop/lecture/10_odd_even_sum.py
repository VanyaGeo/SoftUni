number = int(input())
num_even = 0
num_odd = 0

for num in range (1, number + 1):
    n = int(input())
    if num % 2 == 0:
        num_even += n
    else:
        num_odd += n

if num_even == num_odd:
    print("Yes")
    print(f"Sum = {num_odd}")
else:
    print("No")
    print(f"Diff = {abs(num_odd - num_even)}")
