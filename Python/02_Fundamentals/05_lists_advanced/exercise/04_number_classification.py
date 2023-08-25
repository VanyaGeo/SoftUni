numbers = [number for number in input().split(", ")]

positive = [num for num in numbers if int(num) >= 0]
negative = [num for num in numbers if int(num) < 0]
even = [num for num in numbers if int(num) % 2 == 0]
odd = [num for num in numbers if int(num) % 2 != 0]

positive_n = ", ".join(positive)
negative_n = ", ".join(negative)
even_n = ", ".join(even)
odd_n = ", ".join(odd)

print(f"Positive: {positive_n}")
print(f"Negative: {negative_n}")
print(f"Even: {even_n}")
print(f"Odd: {odd_n}")
