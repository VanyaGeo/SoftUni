import math

all_tournaments = int(input())
beginning_points = int(input())

final_points = beginning_points
win_amount = 0

for i in range(1, all_tournaments + 1):
    stage = input()
    if stage == "W":
        final_points = final_points + 2000
        win_amount = win_amount + 1
    elif stage == "F":
        final_points = final_points + 1200
    elif stage == "SF":
        final_points = final_points + 720

win_percent = win_amount / all_tournaments * 100
average_points = (final_points - beginning_points) / all_tournaments

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(F"{win_percent:.2f}%")
