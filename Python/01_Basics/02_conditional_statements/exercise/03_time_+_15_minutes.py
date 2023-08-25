hours = int(input())
minutes = int(input())

total_minutes = ((hours * 60) + minutes) + 15

final_hours = total_minutes // 60
final_minutes = total_minutes % 60

if final_hours > 23:
    final_hours = 0

print(f"{final_hours}:{final_minutes:02d}")
