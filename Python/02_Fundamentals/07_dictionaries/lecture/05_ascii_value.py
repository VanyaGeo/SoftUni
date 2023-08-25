# my_dict = {key: value for key, value in enumerate(input().split(", "))}
# важно!!!

my_dict = {key: ord(key) for key in input().split(", ")}

print(my_dict)

# a, b, c, a