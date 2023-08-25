num = int(input())
data = int(input())
total_num = 0

while total_num < num:
    total_num += data
    if num <= total_num:
        break
    data = int(input())
print(total_num)

# II.
# num = int(input())
# total_num = 0
#
# while True:
#     data = int(input())
#     total_num += data
#     
#     if total_num >= num:
#         print(total_num)
#         break
