def perfect_number(num):
    valid_divisors = []
    for n in range(1, num):
        if num % n == 0:
            valid_divisors.append(int(n))
    if sum(valid_divisors) == num:
        print("We have a perfect number!")
    elif sum(valid_divisors) != num:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)
