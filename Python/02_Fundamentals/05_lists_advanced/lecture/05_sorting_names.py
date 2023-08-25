# name = input().split(", ")

# sorted_names = sorted(name, key=lambda name_: (-len(name_), name_))
# print(sorted_names)


# по този начин се използва сортиране на имената по дължина (len(name_),
# като се започне от най-дългото (-len(name_),
# и когато имаме две еднакво дълги имена, сортираме по азбучен ред (...name_)


names = input().split(", ")

names.sort()
names.sort(key=len, reverse=True)

print(names)