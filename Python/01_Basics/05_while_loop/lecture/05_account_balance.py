amount = input()

total = 0

while amount != "NoMoreMoney":
    number = float(amount)
    if number > 0:
        print(f"Increase: {number:.2f}")
    elif number < 0:
        print("Invalid operation!")
        break
    amount = input()

    total = total + number
print(f"Total: {total:.2f}")


