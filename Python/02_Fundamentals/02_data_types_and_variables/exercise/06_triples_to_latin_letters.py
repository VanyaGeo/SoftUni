number = int(input())

for first_place in range(0, number):
    for second_place in range(0, number):
        for third_place in range(0, number):
            result = chr(97 + first_place) + chr(97 + second_place) + chr(97 + third_place)
            print(result)
