from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
copy_pumps_data = pumps_data.copy()
gas_in_tank = 0
current_pump = 0

while copy_pumps_data:
    petrol, distance = copy_pumps_data.popleft()
    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps_data.rotate(-1)
        copy_pumps_data = pumps_data.copy()
        current_pump += 1
        gas_in_tank = 0

print(current_pump)
