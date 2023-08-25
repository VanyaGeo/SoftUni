groups = int(input())

total_people = 0
musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(1, groups + 1):
    people_in_group = int(input())
    total_people = total_people + people_in_group
    if people_in_group <= 5:
        musala = musala + people_in_group
    elif people_in_group <= 12:
        montblanc = montblanc + people_in_group
    elif people_in_group <= 25:
        kilimanjaro = kilimanjaro + people_in_group
    elif people_in_group <= 40:
        k2 = k2 + people_in_group
    elif people_in_group >= 41:
        everest = everest + people_in_group

percent_musala = musala / total_people * 100
percent_montblanc = montblanc / total_people * 100
percent_kilimanjaro = kilimanjaro / total_people * 100
percent_k2 = k2 / total_people * 100
percent_everest = everest / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_montblanc:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")