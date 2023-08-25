# I
n = int(input())
for num in range(0, n+1):
    if num % 2 == 0:   # num -> в този случай е степента
        a = pow(2, num)   # pow -> в скобите се пише числото, което искаме да повдигнем на някаква степен /
        print(a)                 # и степента, на която искаме да повдигнем числото

#II
number = int(input())
for num in range(0, number + 1):
    if num % 2 == 0:
        print(2 ** num)


#III
number1 = int(input())
for num in range(0, number1 + 1, 2):
    print(2 ** num)
