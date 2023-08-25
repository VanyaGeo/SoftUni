from collections import deque

box_of_clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
current_capacity = rack_capacity
rack_amount = 1
copy_box_of_clothes = box_of_clothes.copy()

for cloth in copy_box_of_clothes:
    if cloth <= current_capacity:
        box_of_clothes.pop()
        current_capacity -= cloth
    else:
        rack_amount += 1
        current_capacity = rack_capacity
        current_capacity -= cloth
        box_of_clothes.pop()

print(rack_amount)