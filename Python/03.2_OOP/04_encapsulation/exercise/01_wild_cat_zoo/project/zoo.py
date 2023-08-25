class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            # animal__class__.__name__ => type of animal (Lion/Tiger/Cheetah)
            # type(animal).__name__ != type of animal (Lion/Tiger/Cheetah) !!!!!
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for worker in self.workers:
            total_salary += worker.salary
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_needed_money = 0
        for animal in self.animals:
            total_needed_money += animal.money_for_care
        if self.__budget >= total_needed_money:
            self.__budget -= total_needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]

        # lions = [repr(animal) for animal in self.animals if isinstance(animal, Lion)]
        # tigers = [repr(animal) for animal in self.animals if isinstance(animal, Tiger)]
        # cheetahs = [repr(animal) for animal in self.animals if isinstance(animal, Cheetah)]

        lions = [lion for lion in self.animals if lion.__class__.__name__ == "Lion"]
        tigers = [tiger for tiger in self.animals if tiger.__class__.__name__ == "Tiger"]
        cheetahs = [cheetah for cheetah in self.animals if cheetah.__class__.__name__ == "Cheetah"]

        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(f"{lion}")

        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(f"{tiger}")

        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(f"{cheetah}")

        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]

        # keepers = [repr(worker) for worker in self.workers if isinstance(worker, Keeper)]
        # caretakers = [repr(worker) for worker in self.workers if isinstance(worker, Caretaker)]
        # vets = [repr(worker) for worker in self.workers if isinstance(worker, Vet)]

        keepers = [keeper for keeper in self.workers if keeper.__class__.__name__ == "Keeper"]
        caretakers = [caretaker for caretaker in self.workers if caretaker.__class__.__name__ == "Caretaker"]
        vets = [vet for vet in self.workers if vet.__class__.__name__ == "Vet"]

        result.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            result.append(f"{keeper}")

        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(f"{caretaker}")

        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(f"{vet}")

        return "\n".join(result)

