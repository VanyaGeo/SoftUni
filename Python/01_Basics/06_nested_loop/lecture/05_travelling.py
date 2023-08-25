# while True:
#     destination = input()
#     if destination == "End":
#         break
#     saved_money = 0
#     budget = float(input())
#     while True:
#         money = float(input())
#         saved_money += money
#         if saved_money >= budget:
#             print(f"Going to {destination}!")
#             break


destination = input()
while destination != "End":
    saved_money = 0
    budget = float(input())
    while budget > saved_money:
        money = float(input())
        saved_money += money

    print(f"Going to {destination}!")
    destination = input()