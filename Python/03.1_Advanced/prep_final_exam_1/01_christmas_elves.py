from collections import deque

elf_energy = deque(int(x) for x in input().split())
number_of_materials = deque(int(x) for x in input().split())

total_energy = 0
toys = 0

attempt = 1

while elf_energy and number_of_materials:

    cur_energy = elf_energy.popleft()
    if cur_energy < 5:
        continue
    cur_material = number_of_materials.pop()

    if attempt % 3 == 0 and attempt % 5 == 0:
        if cur_energy >= cur_material * 2:
            cur_energy -= cur_material * 2
            elf_energy.append(cur_energy)
            total_energy += cur_material * 2
        else:
            number_of_materials.append(cur_material)
            elf_energy.append(cur_energy * 2)

    elif attempt % 3 == 0:
        if cur_energy >= cur_material * 2:
            cur_energy -= cur_material * 2
            elf_energy.append(cur_energy + 1)
            toys += 2
            total_energy += cur_material * 2
        else:
            number_of_materials.append(cur_material)
            elf_energy.append(cur_energy * 2)

    elif attempt % 5 == 0:
        if cur_energy >= cur_material:
            cur_energy -= cur_material
            elf_energy.append(cur_energy)
            total_energy += cur_material
        else:
            number_of_materials.append(cur_material)
            elf_energy.append(cur_energy * 2)

    else:
        if cur_energy >= cur_material:
            cur_energy -= cur_material
            elf_energy.append(cur_energy + 1)
            toys += 1
            total_energy += cur_material
        else:
            number_of_materials.append(cur_material)
            elf_energy.append(cur_energy * 2)

    attempt += 1

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if elf_energy:
    print(f"Elves left: {', '.join([str(x) for x in elf_energy])}")

if number_of_materials:
    print(f"Boxes left: {', '.join([str(x) for x in number_of_materials])}")
