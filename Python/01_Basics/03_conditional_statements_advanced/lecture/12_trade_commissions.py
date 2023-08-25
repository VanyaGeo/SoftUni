city = input()
amount_trades = float(input())
commission = 0
# 0 ≤ s ≤ 500 500 < s ≤ 1 000 1 000 < s ≤ 10 000 s > 10 000

if city == "Sofia":
    if 0 <= amount_trades <= 500:
        commission = amount_trades * 0.05
    elif 500 < amount_trades <= 1000:
        commission = amount_trades * 0.07
    elif 1000 < amount_trades <= 10000:
        commission = amount_trades * 0.08
    elif amount_trades > 10000:
        commission = amount_trades * 0.12

elif city == "Varna":
    if 0 <= amount_trades <= 500:
        commission = amount_trades * 0.045
    elif 500 < amount_trades <= 1000:
        commission = amount_trades * 0.075
    elif 1000 < amount_trades <= 10000:
        commission = amount_trades * 0.10
    elif amount_trades > 10000:
        commission = amount_trades * 0.13

elif city == "Plovdiv":
    if 0 <= amount_trades <= 500:
        commission = amount_trades * 0.055
    elif 500 < amount_trades <= 1000:
        commission = amount_trades * 0.08
    elif 1000 < amount_trades <= 10000:
        commission = amount_trades * 0.12
    elif amount_trades > 10000:
        commission = amount_trades * 0.145

if commission == 0:
    print("error")
else:
    print(f"{commission:.2f}")
