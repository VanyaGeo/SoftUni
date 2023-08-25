class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        self.species = species
        self.name = name
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        self.species = species
        result = ""
        if species == "mammal":
            result = f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result = f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result = f"Birds in {self.zoo_name}: {', '.join(self.birds)}"

        return f"""{result}
Total animals: {Zoo.__animals}"""


name_zoo = input()
zoo = Zoo(name_zoo)
lines = int(input())

for line in range(1, lines + 1):
    command = input().split()
    animal_species = command[0]
    animal_name = command[1]
    zoo.add_animals(animal_species, animal_name)


info_species = input()
print(zoo.get_info(info_species))