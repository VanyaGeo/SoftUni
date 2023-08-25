def calculation(opp, first_num, second_num):
    result = 0
    if operator == "add":
        result = first_num + second_num
    elif operator == "subtract":
        result = first_num - second_num
    elif operator == "multiply":
        result = first_num * second_num
    elif operator == "divide":
        result = first_num // second_num
    return result


operator = input()
first_number = int(input())
second_number = int(input())

res = calculation(operator, first_number, second_number)
print(res)

