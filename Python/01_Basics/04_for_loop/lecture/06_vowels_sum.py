# a e i o u
text = input()

vow_sum = 0

for vow in text:
    if vow == "a":
        vow_sum += 1
    elif vow == "e":
        vow_sum += 2
    elif vow == "i":
        vow_sum += 3
    elif vow == "o":
        vow_sum += 4
    elif vow == "u":
        vow_sum += 5
print(vow_sum)
