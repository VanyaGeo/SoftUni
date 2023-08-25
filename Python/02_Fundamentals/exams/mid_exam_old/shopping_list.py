shopping_list = input().split("!")

command_ = input()

while command_ != "Go Shopping!":
    command = command_.split(" ")
    item = command[1]
    if command[0] == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)
        else:
            pass
    elif command[0] == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            pass
    elif command[0] == "Correct":
        old_item = item
        new_item = command[2]
        if old_item in shopping_list:
            shopping_list = [new_item if item == old_item else item for item in shopping_list]
        else:
            pass
    elif command[0] == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)
        else:
            pass
    command_ = input()

result = ", ".join(shopping_list)
print(result)


# II
#
# def product_indx_in_shop_list(list, product):
#     for indx_element in range(len(list)):
#         if list[indx_element] == product:
#             return indx_element
#     return -1
#
#
# shopping_list = input().split("!")
#
# command_ = input()
#
# while command_ != "Go Shopping!":
#     command = command_.split(" ")
#     item = command[1]
#     if command[0] == "Urgent":
#         if item not in shopping_list:
#             shopping_list.insert(0, item)
#         else:
#             pass
#     elif command[0] == "Unnecessary":
#         if item in shopping_list:
#             shopping_list.remove(item)
#         else:
#             pass
#     elif command[0] == "Correct":
#         old_item = item
#         new_item = command[2]
#         indx = product_indx_in_shop_list(shopping_list, old_item)
#         if indx == -1:
#             continue
#         else:
#             shopping_list[indx] = new_item
#     elif command[0] == "Rearrange":
#         if item in shopping_list:
#             shopping_list.remove(item)
#             shopping_list.append(item)
#         else:
#             pass
#     command_ = input()
#
# result = ", ".join(shopping_list)
# print(result)
#
# # III
#
#
# shopping_list = input().split("!")
#
# command_ = input()
#
# while command_ != "Go Shopping!":
#     command = command_.split(" ")
#     item = command[1]
#     if command[0] == "Urgent":
#         if item not in shopping_list:
#             shopping_list.insert(0, item)
#         else:
#             pass
#     elif command[0] == "Unnecessary":
#         if item in shopping_list:
#             shopping_list.remove(item)
#         else:
#             pass
#     elif command[0] == "Correct":
#         old_item = item
#         new_item = command[2]
#         if old_item in shopping_list:
#             indx = shopping_list.index(old_item)
#             shopping_list[indx] = new_item
#         else:
#             pass
#     elif command[0] == "Rearrange":
#         if item in shopping_list:
#             shopping_list.remove(item)
#             shopping_list.append(item)
#         else:
#             pass
#     command_ = input()
#
# result = ", ".join(shopping_list)
# print(result)