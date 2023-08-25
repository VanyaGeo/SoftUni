prime_sum = 0
non_prime_sum = 0

while True:
    number_str = input()

    if number_str == "stop":
        break

    number_int = int(number_str)
    if number_int < 0:
        print(f"Number is negative.")
        continue

    counter = 0

    for i in range(2, number_int + 1):
        if number_int % i == 0:
            counter += 1

    if counter == 1:
        prime_sum = prime_sum + number_int
    else:
        non_prime_sum = non_prime_sum + number_int

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")