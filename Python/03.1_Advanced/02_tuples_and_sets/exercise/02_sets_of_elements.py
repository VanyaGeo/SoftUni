n_length, m_length = [int(x) for x in input().split()]

n_set = set()
m_set = set()

for i in range(n_length):
    num = int(input())
    n_set.add(num)

for i in range(m_length):
    num = int(input())
    m_set.add(num)

print("\n".join([str(x) for x in (n_set.intersection(m_set))]))