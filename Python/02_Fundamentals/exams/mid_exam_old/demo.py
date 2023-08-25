list = [1, 2, 3, 4, 5, 6]
#       -6,-5,-4,-3,-2,-1

for indx in range(len(list)):
    print(indx, end=" ")

for i in list:
    print(i, end=" ")

print(-len((list)))
print(len(list))

#
# if len(list) < strat_indx < -len(list)
# if -len(list) > end_indx > len(list)

# num = (600 - 250) / 250 * 100
# print(f"{num:.2f}")