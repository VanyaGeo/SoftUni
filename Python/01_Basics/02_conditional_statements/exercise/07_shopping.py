budget = float(input())
videocard = int(input())
processor = int(input())
ram = int(input())

videocard_price = videocard * 250
processor_price = processor * (videocard_price * 0.35)
ram_price = ram * (videocard_price * 0.1)

total_price = videocard_price + processor_price +ram_price

if videocard > processor:
    total_price = total_price - (total_price * 0.15)

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")

else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")