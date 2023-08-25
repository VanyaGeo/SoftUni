from collections import deque

food_quantity = int(input())
quantity_per_day = deque([int(x) for x in input().split()])
copy_quantity_per_day = quantity_per_day.copy()

print(max(quantity_per_day))

for food in copy_quantity_per_day:
    if food_quantity >= food:
        food_quantity -= food
        quantity_per_day.popleft()
    else:
        break

if len(quantity_per_day) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in quantity_per_day])}")
