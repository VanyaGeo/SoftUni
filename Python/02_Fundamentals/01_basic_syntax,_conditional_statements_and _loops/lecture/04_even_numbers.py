# n = int(input())
#
# for i in range(1, n+1):
#     number = int(input())
#     if not number % 2 == 0:
#         print(f"{number} is odd!")
#         break
# else:
#     print("All numbers are even.")


n = int(input())

all_numbers_are_even = True

for _ in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        all_numbers_are_even = False
        break
if all_numbers_are_even:
    print("All numbers are even.")
