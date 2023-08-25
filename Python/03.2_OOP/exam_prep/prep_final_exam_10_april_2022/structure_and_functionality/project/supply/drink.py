from project.supply.supply import Supply


class Drink(Supply):
# Each drink has 15 initial units of energy.
    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
