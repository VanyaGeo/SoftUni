lines = int(input())
list_positive_numbers = []
list_negative_numbers = []
positive_numbers_count = 0
negative_sum = 0

for num in range(lines):
    number = int(input())
    if number > 0:
        list_positive_numbers.append(number)
        positive_numbers_count += 1
    if number < 0:
        list_negative_numbers.append(number)
        negative_sum += number

print(list_positive_numbers)
print(list_negative_numbers)
print(f"Count of positives: {positive_numbers_count}") # => print(f"Count of positives: {len(list_positive_numbers)}")
print(f"Sum of negatives: {negative_sum}") # => print(f"Sum of negatives: {sum(list_negative_numbers)}")
