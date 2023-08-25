num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

for a in range(2, num_1 + 1, 2):
    for b in range(2, num_2 + 1):
        for c in range(2, num_3 + 1, 2):
            if b == 2 or b == 3 or b == 5 or b == 7:
                print(f"{a} {b} {c}")
