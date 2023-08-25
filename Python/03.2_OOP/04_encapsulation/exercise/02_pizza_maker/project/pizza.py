from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name, dough: Dough, max_number_of_toppings):
        self.name= name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) == 0:
            raise ValueError("The name cannot be an empty string")
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_dough):
        if new_dough is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = new_dough

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, new_max_number_of_toppings):
        if new_max_number_of_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = new_max_number_of_toppings

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.max_number_of_toppings:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight

        elif self.max_number_of_toppings > len(self.toppings):
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())



