weekday = input()
ticket_price = 0

if weekday == "Monday" or weekday == "Tuesday" or weekday == "Friday":
    ticket_price = 12

elif weekday == "Wednesday" or weekday == "Thursday":
    ticket_price = 14

else:
    ticket_price = 16

print(ticket_price)
