project_type = input()
row = int(input())
column = int(input())
price = 0

if project_type == "Premiere":
    price = 12.00
elif project_type == "Normal":
    price = 7.50
elif project_type == "Discount":
    price = 5.00

expenses = row * column * price
print(f"{expenses:.2f} leva")
