class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.current_count:
            raise StopIteration
        num = self.count
        self.count -= 1
        return num


# iterator = countdown_iterator(10)
# for item in iterator:
#     print(item, end=" ")
#
# iterator = countdown_iterator(0)
# for item in iterator:
#     print(item, end=" ")
