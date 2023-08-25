def print_rhombus(n):

    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '* ' * i)


number = int(input())

print_rhombus(number)


#II

def print_rhombus(n):

    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print(*['*'] * i)

    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        print(*['*'] * i)


number = int(input())

print_rhombus(number)