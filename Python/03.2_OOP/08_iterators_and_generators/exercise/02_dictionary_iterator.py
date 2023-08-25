class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.dictionary):
            raise StopIteration

        current_index = self.index
        self.index += 1
        key = self.keys[current_index]
        value = self.dictionary[key]
        return key, value


# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
#
# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)
