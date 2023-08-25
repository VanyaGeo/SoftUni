first_seq = set([int(x) for x in input().split()])
second_seq = set([int(x) for x in input().split()])

n_lines = int(input())

for i in range(n_lines):
    info = input().split()
    command = info[0] + " " + info[1]
    if command == "Add First":
        for num in info[2::]:
            first_seq.add(int(num))
    elif command == "Add Second":
        for num in info[2::]:
            second_seq.add(int(num))
    elif command == "Remove First":
        for num in info[2::]:
            first_seq.discard(int(num))
    elif command == "Remove Second":
        for num in info[2::]:
            second_seq.discard(int(num))
    elif command == "Check Subset":
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print("True")
        else:
            print("False")

print(*sorted(first_seq), sep=", ")
print(*sorted(second_seq), sep=", ")

# print(", ".join(sorted([str(x) for x in first_seq])))
# print(", ".join(sorted([str(x) for x in second_seq])))
# --> this is a not working print() because when joining the elements the ordering may not be consistent, leading to
# incorrect output.
