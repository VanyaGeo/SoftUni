def reverse_text(some_text):
    start_idx = len(some_text) - 1
    end_idx = 0
    while start_idx >= end_idx:
        yield some_text[start_idx]
        start_idx -= 1


for char in reverse_text("step"):
    print(char, end='')
