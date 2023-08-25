from collections import deque

customers_name = input()
customers_que = deque()

while customers_name != "End":

    if customers_name != "Paid":
        customers_que.append(customers_name)
    else:
        while customers_que:
            print(customers_que.popleft())

    customers_name = input()

else:
    print(f"{len(customers_que)} people remaining.")