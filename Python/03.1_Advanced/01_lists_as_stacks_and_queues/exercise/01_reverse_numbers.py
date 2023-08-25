# I
# stack_numbers = [num for num in input().split()]
# stack_numbers.reverse()
# print(*stack_numbers, sep=" ")

# II

from collections import deque

deque = deque([num for num in input().split()]) # => deque = deque(input().split())

for i in range(len(deque)):
    print(deque.pop(), end=" ")

