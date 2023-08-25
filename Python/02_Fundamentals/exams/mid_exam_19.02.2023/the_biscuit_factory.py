import math

biscuits_per_day_per_worker = int(input())
amount_of_workers = int(input())
competing_factory = int(input())

final_amount_biscuits = 0
usual_amount = 0

for day in range(1, 31):
    if day % 3 == 0:
        usual_amount = math.floor(biscuits_per_day_per_worker * 0.75 * amount_of_workers)
    else:
        usual_amount = biscuits_per_day_per_worker * amount_of_workers
    final_amount_biscuits += usual_amount

print(f"You have produced {final_amount_biscuits} biscuits for the past month.")

if final_amount_biscuits > competing_factory:
    percentage = (final_amount_biscuits - competing_factory) / competing_factory * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")

else:
    percentage = (competing_factory - final_amount_biscuits) / competing_factory * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")
