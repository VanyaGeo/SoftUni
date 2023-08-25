number_of_rooms = int(input())
free_chairs_total = 0
needed_chairs = 0

for room in range(1, number_of_rooms + 1):
    information = input().split()
    chairs = len(information[0])
    people = int(information[1])
    free_chairs = 0

    if chairs >= people:
        free_chairs = chairs - people
    elif chairs < people:
        needed_chairs = people - chairs
        print(f"{needed_chairs} more chairs needed in room {room}")

    free_chairs_total += free_chairs

if free_chairs_total >= 0 and needed_chairs == 0:
    print(f"Game On, {free_chairs_total} free chairs left")

