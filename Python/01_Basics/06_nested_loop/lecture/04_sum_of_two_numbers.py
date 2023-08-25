# first_number = int(input())
# second_number = int(input())
# magic_number = int(input())
# combination = 0
# result = 0
# for n1 in range(first_number, second_number+1):
#     for n2 in range(first_number, second_number+1):
#         result = n1 + n2
#         combination += 1
#         if result == magic_number:
#             print(f"Combination N:{combination} ({n1} + {n2} = {magic_number})")
#             break
#     if result == magic_number:
#         break
#
# if result != magic_number:
#     print(f"{combination} combinations - neither equals {magic_number}")
#
#
#
first_number = int(input())
second_number = int(input())
magic_number = int(input())
combination = 0

success = False   # success = flag
for n1 in range(first_number, second_number+1):
    for n2 in range(first_number, second_number+1):
        result = n1 + n2
        combination += 1
        if result == magic_number:
            print(f"Combination N:{combination} ({n1} + {n2} = {magic_number})")
            success = True
            break
    if success:
        break
if not success:  #по този начин придобива повече смисъл
    print(f"{combination} combinations - neither equals {magic_number}")

