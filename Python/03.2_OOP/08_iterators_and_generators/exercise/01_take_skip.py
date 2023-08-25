class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_idx = 0
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx >= self.count:
            raise StopIteration
        number = self.current_num
        self.current_num += self.step
        self.current_idx += 1
        return number


# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
#
#
# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
