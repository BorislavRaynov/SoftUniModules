class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if price < self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        current_payable_amount = 0
        for worker in self.workers:
            current_payable_amount += worker.salary

        if current_payable_amount <= self.__budget:
            self.__budget -= current_payable_amount
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_amount = 0
        for animal in self.animals:
            needed_amount += animal.money_for_care

        if needed_amount <= self.__budget:
            self.__budget -= needed_amount
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        amount_of_lions = 0
        amount_of_tigers = 0
        amount_of_cheetahs = 0
        lions_info = ""
        tigers_info = ""
        cheetahs_info = ""
        animals_info = ""

        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                amount_of_lions += 1
                lions_info += f"\n{animal.__repr__()}"
            elif animal.__class__.__name__ == "Tiger":
                amount_of_tigers += 1
                tigers_info += f"\n{animal.__repr__()}"
            else:
                amount_of_cheetahs += 1
                cheetahs_info += f"\n{animal.__repr__()}"

        animals_info += f"You have {len(self.animals)} animals"
        animals_info += f"\n----- {amount_of_lions} Lions:"
        animals_info += lions_info
        animals_info += f"\n----- {amount_of_tigers} Tigers:"
        animals_info += tigers_info
        animals_info += f"\n----- {amount_of_cheetahs} Cheetahs:"
        animals_info += cheetahs_info

        return animals_info

    def workers_status(self):
        amount_of_keepers = 0
        amount_of_caretakers = 0
        amount_of_vets = 0
        keepers_info = ""
        caretakers_info = ""
        vets_info = ""
        workers_info = ""

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                amount_of_keepers += 1
                keepers_info += f"\n{worker.__repr__()}"
            elif worker.__class__.__name__ == "Caretaker":
                amount_of_caretakers += 1
                caretakers_info += f"\n{worker.__repr__()}"
            else:
                amount_of_vets += 1
                vets_info += f"\n{worker.__repr__()}"

        workers_info += f"You have {len(self.workers)} workers"
        workers_info += f"\n----- {amount_of_keepers} Keepers:"
        workers_info += keepers_info
        workers_info += f"\n----- {amount_of_caretakers} Caretakers:"
        workers_info += caretakers_info
        workers_info += f"\n----- {amount_of_vets} Vets:"
        workers_info += vets_info

        return workers_info
