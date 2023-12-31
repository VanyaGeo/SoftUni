class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# Implement the needed magic methods so that:
    # • Each person could be represented by their names, separated by a single space.
    # • When you concatenate two people, you should return a new instance of a person who will take the first
    # name from the first person and the surname from the second person.

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):  # concatenate two groups/instances/...
        return Person(self.name, other.surname) # return a new instance


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

# . Implement the needed magic methods so that:
    # • When you access the length of a group instance, you should receive the total number of people in the group.
    # • When you concatenate two groups, you should return a new instance of a group which will have a name - string in
    # the format "{first_name} {second_name}" and all the people in the two groups will participate in the new one too.
    # • Each group should be represented in the format "Group {name} with members {members' names separated by ", "}"
    # • You could iterate over a group, and each person (element of the group) should be represented in the
    # format "Person {index}: {person's name}"

    def __len__(self):  # access length
        return len(self.people)

    def __add__(self, other):  # concatenate two groups/instances/...
        new_name = f"{self.name} {other.name}"
        new_people = self.people + other.people
        return Group(new_name, new_people) # return a new instance

    def __repr__(self):
        members = ", ".join(str(person) for person in self.people)
        return f"Group {self.name} with members {members}"

    def __getitem__(self, idx):  #-> това може да стане и с долните два метода:
        return f"Person {idx}: {self.people[idx]}"


#     def __iter__(self):
#         new_people = [f"Person {self.people.index(person)} {person}" for person in self.people]
#         return iter(new_people)
#
#     def __getitem__(self, item:int):
#         wanted_person = self.people[item]
#         return f"Person {self.people.index(wanted_person)} {wanted_person}"


# p0 = Person('Aliko', 'Dangote')
# p1 = Person('Bill', 'Gates')
# p2 = Person('Warren', 'Buffet')
# p3 = Person('Elon', 'Musk')
# p4 = p2 + p3
# first_group = Group('__VIP__', [p0, p1, p2])
# second_group = Group('Special', [p3, p4])
# third_group = first_group + second_group
# print(len(first_group))
# print(second_group)
# print(third_group[0])
# for person in third_group:
#     print(person)

