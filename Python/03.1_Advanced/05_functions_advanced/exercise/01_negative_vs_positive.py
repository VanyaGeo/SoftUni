all_numbers = [int(x) for x in input().split()]

negative_numbers = [x for x in all_numbers if x < 0]
positive_numbers = [x for x in all_numbers if x > 0]

print(sum(negative_numbers))
print(sum(positive_numbers))

if abs(sum(negative_numbers)) > sum(positive_numbers):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")