number = int(input())
tank_capacity = 255
water_sum = 0

for line in range(1, number + 1):
    water = int(input())
    water_sum += water
    if water_sum > tank_capacity:
        print("Insufficient capacity!")
        water_sum -= water

print(water_sum)
