def squares(num):
    start_num = 1
    while start_num <= num:
    # for i in range(start_num, num + 1):
        yield (start_num ** 2)
        start_num += 1


print(list(squares(5)))