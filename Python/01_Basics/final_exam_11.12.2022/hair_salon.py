goal = int(input())
price = 0

while price < goal:
    service = input()
    if service == "haircut":
        type = input()
        if type == "mens":
            price = price + 15
        elif type == "ladies":
            price = price + 20
        elif type == "kids":
            price = price + 10
    elif service == "color":
        type = input()
        if type == "touch up":
            price = price + 20
        elif type == "full color":
            price = price + 30
    elif service == "closed":
        diff = abs(price - goal)
        print(f"Target not reached! You need {diff}lv. more.")
        print(f"Earned money: {price}lv.")
        break

if price >= goal:
    print("You have reached your target for the day!")
    print(f"Earned money: {price}lv.")
