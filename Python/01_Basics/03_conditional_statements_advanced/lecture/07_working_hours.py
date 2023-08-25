hour = int(input())
weekday = input()

if weekday == "Sunday":
    print("closed")

elif 10 <= hour <= 18:
    print("open")

else:
    print("closed")
