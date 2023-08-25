from itertools import permutations


def possible_permutations(my_list):
    for el in permutations(my_list):
        yield list(el)  # правим го на лист, защото иначе излиза като тюпъл


# def possible_permutations(my_list: list):
#     if len(my_list) == 0:
#         yield []
#     elif len(my_list) == 1:
#         yield my_list
#     else:
#         for i in range(len(my_list)):
#             for p_p in possible_permutations(my_list[:i] + my_list[i + 1:]):
#                 yield [my_list[i]] + p_p


[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]