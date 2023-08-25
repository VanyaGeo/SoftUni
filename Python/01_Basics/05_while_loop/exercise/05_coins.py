change = float(input())
convert_coins = change * 100
count = 0

while convert_coins != 0:
    if convert_coins >= 200:
        convert_coins -= 200
    elif convert_coins >= 100:
        convert_coins -= 100
    elif convert_coins >= 50:
        convert_coins -= 50
    elif convert_coins >= 20:
        convert_coins -= 20
    elif convert_coins >= 10:
        convert_coins -= 10
    elif convert_coins >= 5:
        convert_coins -= 5
    elif convert_coins >= 2:
        convert_coins -= 2
    elif convert_coins >= 1:
        convert_coins -= 1
    else:
        break
    count += 1

print(count)