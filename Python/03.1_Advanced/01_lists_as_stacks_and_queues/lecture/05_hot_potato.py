from collections import deque

kids = deque(input().split())

number_to_leave = int(input())

while len(kids) > 1:

    kids.rotate(-(number_to_leave-1))
    print(f"Removed {kids.popleft()}")

print(f"Last is {''.join(kids)}")


