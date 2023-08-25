import math

world_record = float(input())
distance = float(input())
time_per_meter = float(input())
delay = (math.floor(distance / 15)) * 12.5

total_time = (distance * time_per_meter) + delay

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - world_record:.2f} seconds slower.")
