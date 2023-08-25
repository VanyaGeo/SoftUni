class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_idx = len(self.iterable) - 1
        self.end_idx = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.start_idx < self.end_idx:
            raise StopIteration
        else:
            self.current_idx = self.start_idx
            self.start_idx -= 1
            return self.iterable[self.current_idx]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

