# import re
#
# command = input()
# pattern = r">>([A-Za-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)"
# bought_items = []
# total_price = 0
#
# while command != "Purchase":
#     match = re.findall(pattern, command)
#     if match:
#         result = match[0]
#         furniture = result[0]
#         price = float(result[1])
#         amount = int(result[2])
#         bought_items.append(furniture)
#         total_price += price * amount
#
#     command = input()
#
# print(f"Bought furniture: ")
# print(*bought_items, sep="\n")
# # print("\n".join(bought_items))
# # for item in bought_items:
# #     print(item)
# print(f"Total money spend: {total_price:.2f}")

# II
import re

command = input()
pattern = r">>([A-Za-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)"
bought_items = []
total_price = 0

while command != "Purchase":
    match = re.search(pattern, command)
    if match:

        furniture, price, amount = match.groups()
        # furniture, price, amount = match.group(1), match.group(2), match.group(3)

        bought_items.append(furniture)
        total_price += float(price) * int(amount)

    command = input()

print(f"Bought furniture: ")
# print(*bought_items, sep="\n")
# print("\n".join(bought_items))
if bought_items:
    print("\n".join(bought_items))
# for item in bought_items:
#     print(item)
print(f"Total money spend: {total_price:.2f}")

# III
#
# import re
#
# command = input()
# pattern = r">>([A-z]+)<<(\d+\.?\d*)!(\d+)"
# bought_items = []
# total_price = 0
#
# while command != "Purchase":
#     matches = re.findall(pattern, command)
#     for match in matches:
#         furniture = match.group(1)
#         price = float(match.group(2))
#         amount = int(match.group(3))
#         bought_items.append(furniture)
#         total_price += price * amount
#
#     command = input()
#
# print(f"Bought furniture: ")
# # print(*bought_items, sep="\n")
# # # print("\n".join(bought_items))
# for item in bought_items:
#     print(item)
# print(f"Total money spend: {total_price:.2f}")


# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase