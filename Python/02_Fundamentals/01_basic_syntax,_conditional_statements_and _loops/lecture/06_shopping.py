# budget = int(input())
#
# total_price = 0
#
# while total_price < budget:
#     command = input()
#     if command != "End":
#         price = int(input())
#         total_price += price
#     if command == "End":
#         print("You bought everything needed.")
#         break
#
budget = int(input())
total_price = 0

command = input()
while command != "End":
    price = int(command)
    total_price += price
    if total_price > budget:
        print("You went in overdraft!")
        break
    command = input()
if command == "End":
    print("You bought everything needed.")
