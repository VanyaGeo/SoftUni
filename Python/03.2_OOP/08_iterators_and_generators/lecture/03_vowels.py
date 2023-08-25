class vowels:
    def __init__(self, some_string):
        self.some_string = some_string
        self.vowels = ['a', 'e', 'i', 'o', 'u']   # и тези: 'A', 'E', 'I', 'O', 'U'
        self.start = 0
        self.end = len(self.some_string) - 1


    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration

        else:
            current_idx = self.start
            self.start += 1
            if self.some_string[current_idx].lower() in self.vowels:
                return self.some_string[current_idx]
            return self.__next__()



my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
