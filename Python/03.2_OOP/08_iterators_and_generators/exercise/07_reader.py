def read_next(*args):
    items = args
    # from seq in items:
    #     yield from seq
    for el in items:
        for i in el:
            yield i


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

