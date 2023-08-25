import math

n_lines = int(input())

set_even_names = set()
set_odd_names = set()

for line in range(1, n_lines+1):
    name = input()
    sum_of_letters = (sum([ord(letter) for letter in name])) // line
    if sum_of_letters % 2 == 0:
        set_even_names.add(sum_of_letters)
    else:
        set_odd_names.add(sum_of_letters)

if sum(set_even_names) == sum(set_odd_names):
    print(*set_even_names.union(set_odd_names), sep=", ")
elif sum(set_even_names) > sum(set_odd_names):
    print(*set_even_names.symmetric_difference(set_odd_names), sep=", ")
else:
    print(*set_odd_names.difference(set_even_names), sep=", ")

