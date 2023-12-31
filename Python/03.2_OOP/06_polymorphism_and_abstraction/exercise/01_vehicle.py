from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
# инит-а си остава със същите параметри като на Vehicle, затова можем да не го изписваме отново тук.
    def drive(self, distance):
        current_consumption = (self.fuel_consumption + 0.9) * distance
        if self.fuel_quantity >= current_consumption:
            self.fuel_quantity -= current_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    def drive(self, distance):
        current_consumption = (self.fuel_consumption + 1.6) * distance
        if self.fuel_quantity >= current_consumption:
            self.fuel_quantity -= current_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


# TEST:

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
