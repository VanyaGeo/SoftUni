# I
tail = input()
body = input()
head = input()

my_list = [tail, body, head]
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)

# II
# my_list = []
# for parts in range(3):
#     part = input()
#     my_list.append(part)
# my_list[0], my_list[2] = my_list[2], my_list[0]
# print(my_list)

# III
# my_list = [input(), input(), input()]
#
# my_list[0], my_list[2] = my_list[2], my_list[0]
#
# print(my_list)