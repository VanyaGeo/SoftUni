# I
#
# def repeat(word, number):
#     result = word * number
#     return result
#
#
# text = input()
# times = int(input())
#
#
# res = repeat(text, times)
# print(res)

# II

# text = input()
# times = int(input())

repeat = lambda word, number: word * number

# result = repeat(text, times)
# print(result)

# print(repeat(text, times))

print(repeat(word=input(), number=int(input())))

