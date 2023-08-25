n_lines = int(input())

element_set = set()

for i in range(n_lines):
    element = input().split()
    for el in element:
        element_set.add(el)

print("\n".join(element_set))