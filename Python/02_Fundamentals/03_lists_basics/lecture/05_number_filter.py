lines = int(input())

even_number_list = []
odd_number_list = []
positive_number_list = []
negative_number_list = []

for index in range(lines):
    number = int(input())
    if number % 2 == 0:
        even_number_list.append(number)
    if number % 2 == 1:
        odd_number_list.append(number)
    if number < 0:
        negative_number_list.append(number)
    if number >= 0:
        positive_number_list.append(number)

command = input()
if command == "even":
    print(even_number_list)
elif command == "odd":
    print(odd_number_list)
elif command == "positive":
    print(positive_number_list)
elif command == "negative":
    print(negative_number_list)
