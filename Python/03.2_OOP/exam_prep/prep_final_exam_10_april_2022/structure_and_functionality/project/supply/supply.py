from abc import ABC, abstractmethod


class Supply(ABC):
# It is a base class of any type of supply, and it should not be able to be instantiated.
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        else:
            self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        else:
            self.__energy = value

    @abstractmethod
    def details(self):
        pass

# Return the supply's type, name and energy in the format: "{type}: {name}, {energy}".
# The type of the supply is either "Food" or "Drink".
# Hint: override the method in the child classes.

