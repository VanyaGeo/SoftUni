numbers_of_guests = int(input())

reservation_numbers = set()

for num in range(numbers_of_guests):
    reservation_code = input()
    reservation_numbers.add(reservation_code)

command = input()

while command != "END":
    reservation_numbers.remove(command)
    command = input()

print(len(reservation_numbers))
print("\n".join(sorted(reservation_numbers)))
