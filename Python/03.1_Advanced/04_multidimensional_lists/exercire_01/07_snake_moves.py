rows, columns = [int(x) for x in input().split()]
snake_text = input()

snake_text_index = 0

for row in range(rows):
    result = ""
    # result = []
    for column in range(columns):
        if snake_text_index == len(snake_text):
            snake_text_index = 0
        if row % 2 == 0:
            result += snake_text[snake_text_index]
            # result.append(snake_text[snake_text_index])
        else:
            result = snake_text[snake_text_index] + result
            # result.insert(0, snake_text[snake_text_index])
        snake_text_index += 1

    print(result)
    # print(*result, sep="")

# II

# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]  # cols = 6
# word = list(input())  # abc => ["a", "b", "c"]
#
# word_copy = deque(word)
#
# for row in range(rows):
#     while len(word_copy) < cols:
#         word_copy.extend(word)
#
#     if row % 2 == 0:
#         print(*[word_copy.popleft() for _ in range(cols)], sep="")
#     else:
#         print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")