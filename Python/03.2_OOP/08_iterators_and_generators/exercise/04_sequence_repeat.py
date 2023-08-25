class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = 0
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number >= self.number:
            raise StopIteration
        current_index = self.index
        self.index += 1
        self.current_number += 1
        if self.index > len(self.sequence) - 1:
            self.index = 0

        return self.sequence[current_index]


# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')
